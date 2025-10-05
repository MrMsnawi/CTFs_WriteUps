#!/usr/bin/env python3

from pwn import *

def print_lines(io):
    info("Printing received lines\n")
    while True:
        try:
            line = io.recvline()
            success(line.decode())
        except EOFError:
            break

context(arch="amd64", os="linux", log_level="info")

program = "/challenge/pwntools-tutorials-level2.3"

p = process(program)

# copy 8-bytes memory starting at 0x404000 to 8-bytes memory starting at 0x405000

#i1 = "mov rax, qword [0x404000]"
#i2 = "mov qword [0x405000], rax"

i1 = "mov rsi, 0x404000"
i2 = "mov rdi, 0x405000"
i3 = "movsd"
c = "; "
code = i1 + c + i2 + c + i3

payload = asm(code)

p.sendafter(b"Please give me your assembly in bytes ", payload)

print_lines(p)
