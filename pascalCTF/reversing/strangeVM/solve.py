pc = 0
mem = bytearray(256)
code = open("code.pascal", "rb").read()

while code[pc] != 0:
    op = code[pc]

    if op == 0x01:  # ADD
        off = read_int(code, pc+1)
        val = code[pc+5]
        mem[off] = (mem[off] + val) & 0xff
        pc += 6

    elif op == 0x02:  # SUB
        off = read_int(code, pc+1)
        val = code[pc+5]
        mem[off] = (mem[off] - val) & 0xff
        pc += 6

    elif op == 0x03:  # MOD
        off = read_int(code, pc+1)
        val = code[pc+5]
        mem[off] %= val
        pc += 6

    elif op == 0x04:  # MOV
        off = read_int(code, pc+1)
        val = code[pc+5]
        mem[off] = val
        pc += 6

    elif op == 0x05:  # INPUT
        pc += 5  # ignore

    elif op == 0x06:  # JZ
        off = read_int(code, pc+1)
        jmp = code[pc+5]
        if mem[off] == 0:
            pc += jmp
        pc += 5

print(mem.split(b"\x00")[0])

