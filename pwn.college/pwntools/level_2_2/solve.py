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

program = "./pwntools-tutorials-level2.2"

p = process(program)

# rax = rax % rbx + rcx - rsi

i1 = "div rbx"
i2 = "add rdx, rcx"
i3 = "sub rdx, rsi"
i4 = "mov rax, rdx"
c = "; "
code = i1 + c + i2 + c + i3 + c + i4

payload = asm(code)

p.sendafter(b"Please give me your assembly in bytes ", payload)

print_lines(p)
