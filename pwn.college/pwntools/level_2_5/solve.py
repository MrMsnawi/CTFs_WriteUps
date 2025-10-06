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

program = "/challenge/pwntools-tutorials-level2.5"

p = process(program)

# the top value of the stack = abs(the top value of the stack)

i1 = "pop rax"
i2 = "cmp rax, 0"
i3 = "jg .done"
i4 = "imul rax, -1"
i5 = ".done:"
i6 = "push rax"

c = "; "
code = i1 + c + i2 + c + i3 + c + i4 + c + i5 + c + i6

payload = asm(code)

p.sendafter(b"Please give me your assembly in bytes ", payload)

print_lines(p)
