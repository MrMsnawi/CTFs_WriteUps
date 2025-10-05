#!/usr/bin/env python3

from pwn import *

def print_lines(p):
    info("Printing received lines\n")
    while True:
        try:
            line = p.recvline()
            success(line.decode())
        except EOFError:
            break

context(arch="amd64", os="linux", log_level="info")

program = "./pwntools-tutorials-level2.0"

p = process(program)

payload = asm("mov rax, 0x12345678")
#payload += b"\n"

p.sendafter(b"Please give me your assembly in bytes ", payload)

print_lines(p)
