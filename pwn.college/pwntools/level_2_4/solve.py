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

program = "/challenge/pwntools-tutorials-level2.4"

p = process(program)

# the top value of the stack = the top value of the stack - rbx

i1 = "pop rax"
i2 = "sub rax, rbx"
i3 = "push rax"

c = "; "
code = i1 + c + i2 + c + i3

payload = asm(code)

p.sendafter(b"Please give me your assembly in bytes ", payload)

print_lines(p)
