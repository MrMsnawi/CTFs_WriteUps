# CrackMe Writeup: easy_reverse (cbm-hackers)

**Platform:** crackmes.one | **Difficulty:** 1 | **Arch:** x86-64 Linux | **Author:** cbm-hackers

---

## Recon

```bash
$ file rev50_linux64-bit
rev50_linux64-bit: ELF 64-bit LSB pie executable, x86-64, dynamically linked, not stripped
```

Not stripped — function names are visible. Running `strings` reveals key strings: `"Nice Job!!"`, `"flag{%s}"`, `"try again!"`, and the source file name `rev_50.c`.

## Static Analysis

Disassembling `main` in GDB, the validation logic boils down to two checks:

**Check 1 — Length must be 10:**
```asm
call   strlen@plt
cmp    rax, 0xa          ; strlen(argv[1]) == 10?
jne    <fail>
```

**Check 2 — 5th character (index 4) must be `@` (0x40):**
```asm
add    rax, 0x4          ; argv[1] + 4
movzx  eax, BYTE PTR [rax]
cmp    al, 0x40          ; password[4] == '@'?
jne    <fail>
```

If both pass → prints `"Nice Job!!"` then `flag{<your_input>}`.

## Solution

Any 10-character string with `@` at index 4 works:

```bash
$ ./rev50_linux64-bit 0123@56789
Nice Job!!
flag{0123@56789}
```

## Tools Used

`file`, `strings`, `ltrace`, `gdb` (pwndbg)
