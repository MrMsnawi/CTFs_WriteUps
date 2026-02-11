# lonely_bot - Reversing Challenge Writeup

**Challenge Category**: Reverse Engineering  
**Difficulty**: Medium  
**Flag**: `bctf{Th4t5_a_n1C3_NuMB3r}`

## Challenge Description

```
I don't know anyone with the same favorite number as me :(
```

We're given a binary called `lonely_bot` that asks for our "favorite number" and we need to find the correct one.

---

## Table of Contents

1. [Initial Reconnaissance](#initial-reconnaissance)
2. [Static Analysis - Discovering the VM](#static-analysis---discovering-the-vm)
3. [Understanding the VM Bytecode](#understanding-the-vm-bytecode)
4. [Decoding the VM Logic](#decoding-the-vm-logic)
5. [Finding the Secret](#finding-the-secret)
6. [Solution](#solution)
7. [Tools Used](#tools-used)
8. [Key Takeaways](#key-takeaways)

---

## Initial Reconnaissance

First, let's check what we're dealing with:

```bash
$ file lonely_bot
lonely_bot: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, 
interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1d9362a9b9033f3a19668652211646b0204debe5, 
for GNU/Linux 3.2.0, stripped
```

Key observations:
- 64-bit Linux executable
- Dynamically linked
- **Stripped** (no debugging symbols - this will make reversing harder)
- PIE executable (Position Independent Executable)

Let's run it to see its behavior:

```bash
$ echo "42" | ./lonely_bot
What's your favorite number? :D
Ah, a fan of "42"...
Goodbye.

$ echo "1337" | ./lonely_bot
What's your favorite number? :D
Ah, a fan of "1337"...
Goodbye.
```

**Observation**: The program accepts any input and responds the same way. This suggests there's a specific value that will trigger different behavior (likely revealing the flag).

Let's check the imported functions:

```bash
$ readelf -s lonely_bot | grep UND
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strchr@GLIBC_2.2.5
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.2.5
     5: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND read@GLIBC_2.2.5
     7: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strcmp@GLIBC_2.2.5
     9: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5
    11: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND sleep@GLIBC_2.2.5
```

The `strcmp` function is interesting - this is likely where our input is compared against the expected value.

---

## Static Analysis - Discovering the VM

Using `objdump -M intel -d lonely_bot`, we disassemble the binary. The entry point leads us to a function at `0x2154` (this is main, though it's not labeled due to stripping).

### The Initialization Loop

The main function contains an interesting loop:

```asm
2154:   push   rbp
2158:   mov    rbp, rsp
215c:   mov    QWORD PTR [rbp-0x8], 0x0
2164:   jmp    21a3

; Loop body
2166:   mov    rax, QWORD PTR [rbp-0x8]
216a:   mov    rdx, QWORD PTR [rbp-0x8]
216e:   add    rdx, 0x2
2172:   lea    rcx, [rdx*8+0x0]
217a:   lea    rdx, [rbp-0x8]
217e:   add    rdx, rcx
2181:   lea    rcx, [rax*8+0x0]
2189:   lea    rax, [rip+0x2e90]        ; 0x5020 <- Important!
2190:   mov    rax, QWORD PTR [rcx+rax*1]
2194:   mov    QWORD PTR [rdx], rax
2197:   mov    rax, QWORD PTR [rbp-0x8]
219b:   add    rax, 0x1
219f:   mov    QWORD PTR [rbp-0x8], rax

; Loop condition
21a3:   mov    rax, QWORD PTR [rbp-0x8]
21a7:   cmp    rax, 0x9e                ; Loop 158 (0x9e) times
21ad:   jbe    2166
```

**Analysis**: This loop runs 158 times, loading data from address `0x5020` and building something on the stack. This is unusual and suggests some form of self-modifying code or a VM.

### Examining the Data at 0x5020

Let's look at what's stored at `0x5020`:

```python
import struct

with open('lonely_bot', 'rb') as f:
    data = f.read()

# 0x5020 in memory corresponds to file offset 0x4020
offset = 0x4020
for i in range(20):
    ptr = int.from_bytes(data[offset:offset+8], 'little')
    print(f"[{i:3d}] {hex(ptr):18s}")
    offset += 8
```

Output:
```
[  0] 0x212f            
[  1] 0x5560            
[  2] 0x212d            
[  3] 0x7920732774616857
[  4] 0x2131            
...
```

Some of these values look like addresses in the code section (`0x2129`, `0x212d`, `0x212f`). Let's check what's at those addresses:

```bash
$ objdump -M intel -d lonely_bot | grep -A1 "2129:"
2129:   5f                      pop    rdi
212a:   c3                      ret

$ objdump -M intel -d lonely_bot | grep -A1 "212b:"
212b:   5e                      pop    rsi
212c:   c3                      ret

$ objdump -M intel -d lonely_bot | grep -A1 "212d:"
212d:   5a                      pop    rdx
212e:   c3                      ret

$ objdump -M intel -d lonely_bot | grep -A1 "212f:"
212f:   58                      pop    rax
2130:   c3                      ret
```

**Eureka!** These are **ROP gadgets** - small instruction sequences ending in `ret`. This is characteristic of:
1. Return-Oriented Programming exploits, OR
2. A bytecode-based virtual machine

Given the context of a CTF challenge, this is almost certainly a **VM implementation using ROP chains**.

### Complete Gadget List

```asm
0x2129:  pop    rdi; ret             ; Load first function argument
0x212b:  pop    rsi; ret             ; Load second function argument
0x212d:  pop    rdx; ret             ; Load third function argument
0x212f:  pop    rax; ret             ; Load value into rax
0x2131:  mov    QWORD PTR [rax], rdx; ret   ; Write memory
0x2135:  mov    rsi, QWORD PTR [rsi]; ret   ; Read memory
0x2139:  xor    QWORD PTR [rax], rsi; ret   ; XOR operation
0x213d:  test   rax, rax; jne +4; add rsp, 8; ret    ; Conditional
0x2147:  test   rax, rax; jne -10; add rsp, 0x1a0; ret  ; Loop/call
```

---

## Understanding the VM Bytecode

Now that we know it's a VM, let's decode the bytecode to understand what the program actually does.

### Bytecode Decoder Script

```python
#!/usr/bin/env python3
import struct

with open('lonely_bot', 'rb') as f:
    data = f.read()

# Extract bytecode starting from file offset 0x4020
offset = 0x4020
bytecode = []

for i in range(160):  # Decode up to position 160
    ptr = int.from_bytes(data[offset:offset+8], 'little')
    bytecode.append(ptr)
    offset += 8

# Gadget dictionary for pretty printing
gadgets = {
    0x2129: "pop rdi; ret",
    0x212b: "pop rsi; ret",
    0x212d: "pop rdx; ret",
    0x212f: "pop rax; ret",
    0x2131: "mov [rax], rdx; ret",
    0x2135: "mov rsi, [rsi]; ret",
    0x2139: "xor [rax], rsi; ret",
    0x213d: "test rax; conditional",
    0x2147: "strcmp/call",
    0x2146: "ret",
}

# Print the bytecode
for i in range(len(bytecode)):
    val = bytecode[i]
    desc = ""
    
    if val in gadgets:
        desc = f"  // {gadgets[val]}"
    elif val > 0x5000:
        desc = f"  // data @ {hex(val)}"
    elif val < 0x1000:
        desc = f"  // immediate value"
        
    print(f"[{i:3d}] {hex(val):18s}{desc}")
```

### Key Bytecode Sections

**Section 1: Building the prompt** (positions 0-20)

The bytecode constructs the string "What's your favorite number? :D" by loading string fragments:

```python
# Example: Decode a string value
val = 0x7920732774616857
decoded = struct.pack('<Q', val).decode('ascii')
print(decoded)  # "What's y"
```

**Section 2: Reading user input** (positions 20-43)

The VM calls `read()` to get user input and stores it at memory address `0x5540`.

**Section 3: The comparison logic** (positions 44-68)

This is where the magic happens:

```
[44] 0x212f              // pop rax
[45] 0x5560              // data @ 0x5560
[46] 0x212d              // pop rdx
[47] 0x5ce8a297fa50cc11  // Expected value (part 1)
[48] 0x2131              // mov [rax], rdx  -> Write expected value to 0x5560

[49] 0x212f              // pop rax
[50] 0x5540              // data @ 0x5540 (our input location)
[51] 0x212b              // pop rsi
[52] 0x25bccca48c35fd54  // XOR key 1
[53] 0x2139              // xor [rax], rsi  -> XOR our input with key

[54] 0x212f              // pop rax
[55] 0x5568              // data @ 0x5568
[56] 0x212d              // pop rdx
[57] 0x6e8eea35727d      // Expected value (part 2)
[58] 0x2131              // mov [rax], rdx

[59] 0x212f              // pop rax
[60] 0x5548              // data @ 0x5548 (our input + 8)
[61] 0x212b              // pop rsi
[62] 0x20eb9c06215d      // XOR key 2
[63] 0x2139              // xor [rax], rsi  -> XOR second part of input

[64] 0x2129              // pop rdi
[65] 0x5560              // First arg: expected value buffer
[66] 0x212b              // pop rsi
[67] 0x5540              // Second arg: our (XOR'd) input
[68] 0x0                 
[69] 0x2147              // Call strcmp(0x5560, 0x5540)
```

---

## Decoding the VM Logic

From the bytecode analysis, we can see the program's logic:

1. **Stores the expected value** at memory address `0x5560`:
   - Part 1: `0x5ce8a297fa50cc11`
   - Part 2: `0x6e8eea35727d`

2. **XORs our input** with specific keys:
   - Input at `0x5540` XOR'd with `0x25bccca48c35fd54`
   - Input at `0x5548` XOR'd with `0x20eb9c06215d`

3. **Compares** the XOR'd input against the expected value using `strcmp()`

The key insight: **Our input is XOR'd before comparison!**

### The XOR Relationship

```
our_input XOR key = expected_value
```

To find the correct input, we reverse the XOR:

```
our_input = expected_value XOR key
```

(This works because XOR is its own inverse: `A XOR B XOR B = A`)

---

## Finding the Secret

Let's calculate the secret input:

```python
#!/usr/bin/env python3
import struct

# What the program expects to see AFTER our input is XOR'd
expected1 = 0x5ce8a297fa50cc11
expected2 = 0x6e8eea35727d

# The XOR keys applied to our input
key1 = 0x25bccca48c35fd54
key2 = 0x20eb9c06215d

# Calculate the original input
# Since: input XOR key = expected
# Then: input = expected XOR key
secret1 = expected1 ^ key1  
secret2 = expected2 ^ key2

print(f"Part 1: {hex(secret1)}")  # 0x79546e3376653145
print(f"Part 2: {hex(secret2)}")  # 0x4e6576335320

# Decode as little-endian ASCII
secret_bytes = struct.pack('<Q', secret1) + struct.pack('<Q', secret2)
secret = secret_bytes.decode('ascii').rstrip('\x00')

print(f"\nSecret input: '{secret}'")
```

Output:
```
Part 1: 0x79546e3376653145
Part 2: 0x4e6576335320

Secret input: 'E1ev3nTy S3veN'
```

The secret is **"E1ev3nTy S3veN"** - a leetspeak representation of "Eleven Seventy-Seven" (which is indeed a number, matching the challenge theme!)

---

## Solution

Let's verify our solution:

```bash
$ echo "E1ev3nTy S3veN" | ./lonely_bot
What's your favorite number? :D
bctf{Th4t5_a_n1C3_NuMB3r}
```

🎉 **Success!**

**Flag**: `bctf{Th4t5_a_n1C3_NuMB3r}`

---

## Tools Used

1. **file** - Identify binary type
2. **objdump** - Disassemble the binary
3. **readelf** - Examine ELF headers and symbols
4. **radare2** - Alternative disassembler/debugger (optional)
5. **Python** - Bytecode decoding and XOR calculation
6. **strings** - Quick check for readable strings (though not very useful here due to obfuscation)

---

## Key Takeaways

### Reversing Techniques Learned

1. **Recognize obfuscation patterns**: 
   - An initialization loop loading function pointers is suspicious
   - Always investigate unusual setup code

2. **Identify ROP gadgets**:
   - Short instruction sequences ending in `ret`
   - Characteristic of ROP chains and VM implementations
   - Pattern: `pop <reg>; ret` or simple operations + `ret`

3. **Understand VM-based obfuscation**:
   - The binary doesn't execute its logic directly
   - Instead, it interprets bytecode using ROP gadgets
   - The real logic is in the bytecode, not the assembly

4. **Trace data flow, not control flow**:
   - When control flow is obfuscated, follow the data
   - Track: Where does input go? What happens to it? What is it compared against?

5. **Work backwards from checks**:
   - Found `strcmp` in imports
   - Traced back to find what values are being compared
   - Discovered the XOR transformation

6. **Understand transformations**:
   - The XOR operation meant we couldn't just read the expected value
   - Had to reverse the XOR: `input = expected XOR key`
   - XOR is self-inverse, making this straightforward

### General CTF Wisdom

- **Simple binaries can hide complex logic**: Don't judge difficulty by file size
- **Always analyze suspicious initialization code**: Setup is often where obfuscation happens
- **VMs are common in CTFs**: Know the signs (gadgets, bytecode, interpreters)
- **Mathematical transformations are reversible**: XOR, ROT, simple encryption can be undone
- **Static analysis beats dynamic for VMs**: Tracing execution in a VM is painful; decode the bytecode instead

---

## Alternative Approaches

While we solved this with static analysis, here are other valid approaches:

### 1. Dynamic Analysis with GDB/r2

Set a breakpoint on `strcmp` and inspect the arguments:

```bash
# Using GDB
$ gdb ./lonely_bot
(gdb) break strcmp
(gdb) run
(input: test)
(gdb) x/s $rdi  # First argument (expected)
(gdb) x/s $rsi  # Second argument (our XOR'd input)
```

This would reveal the expected value after XOR, from which we could work backwards.

### 2. Brute Force (Not Recommended)

Given the challenge hint about "numbers", one could theoretically brute force:
- Try common CTF numbers (42, 1337, 31337, etc.)
- Try strings that look like numbers ("3l3v3n", etc.)

However, with the space of possible inputs, this is impractical.

### 3. Symbolic Execution

Tools like **angr** can automatically solve for inputs that reach certain code paths:

```python
import angr
import claripy

proj = angr.Project('./lonely_bot')
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)

# Find path that prints the flag
simgr.explore(find=lambda s: b"bctf{" in s.posix.dumps(1))

if simgr.found:
    solution = simgr.found[0]
    print(solution.posix.dumps(0))  # Input that reaches the flag
```

---

## Conclusion

The `lonely_bot` challenge demonstrates that complex-looking binaries can often be solved by:
1. Recognizing the obfuscation technique (VM in this case)
2. Understanding the underlying mechanism (ROP-based bytecode interpreter)
3. Decoding the actual logic (XOR transformation before strcmp)
4. Reversing the transformation mathematically

The challenge's name "lonely_bot" and description about not knowing anyone with the same favorite number hints at the uniqueness of the correct answer - there's exactly one value that makes the bot happy!

---

**Author**: [Your Name]  
**Date**: [Date]  
**Challenge Source**: [CTF Name]

---

## Appendix: Complete Decoder Script

```python
#!/usr/bin/env python3
"""
Complete bytecode decoder and solver for lonely_bot
"""
import struct

def decode_bytecode(filename):
    """Extract and decode VM bytecode"""
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Bytecode starts at file offset 0x4020
    offset = 0x4020
    bytecode = []
    
    for i in range(160):
        ptr = int.from_bytes(data[offset:offset+8], 'little')
        bytecode.append(ptr)
        offset += 8
    
    return bytecode

def find_secret(bytecode):
    """Analyze bytecode to find the secret input"""
    
    # From manual analysis, we know:
    # Position 47: Expected value part 1
    # Position 52: XOR key 1
    # Position 57: Expected value part 2
    # Position 62: XOR key 2
    
    expected1 = bytecode[47]  # 0x5ce8a297fa50cc11
    xor_key1 = bytecode[52]   # 0x25bccca48c35fd54
    expected2 = bytecode[57]  # 0x6e8eea35727d
    xor_key2 = bytecode[62]   # 0x20eb9c06215d
    
    # Calculate secret: input = expected XOR key
    secret1 = expected1 ^ xor_key1
    secret2 = expected2 ^ xor_key2
    
    # Decode as little-endian ASCII
    secret_bytes = struct.pack('<Q', secret1) + struct.pack('<Q', secret2)
    secret = secret_bytes.decode('ascii').rstrip('\x00')
    
    return secret

def main():
    print("[*] Decoding VM bytecode...")
    bytecode = decode_bytecode('lonely_bot')
    
    print("[*] Analyzing comparison logic...")
    secret = find_secret(bytecode)
    
    print(f"\n[+] Secret input found: '{secret}'")
    print(f"\n[*] Test it with: echo \"{secret}\" | ./lonely_bot")

if __name__ == '__main__':
    main()
```

---

*This writeup is intended for educational purposes to demonstrate reverse engineering techniques.*
