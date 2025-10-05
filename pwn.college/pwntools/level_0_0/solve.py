#!/usr/bin/env python3

from pwn import *

context(arch="amd64", os="linux", log_level="info")

p = process("./pwntools-tutorials-level0.0")

payload = b'pokemon\n'

p.sendafter(b":)\n###\n", payload)

flag = p.recvline()

print(f"flag is: {flag}")
