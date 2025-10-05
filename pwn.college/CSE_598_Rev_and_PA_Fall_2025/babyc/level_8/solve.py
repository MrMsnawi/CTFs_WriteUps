#!/usr/bin/env python3

from pwn import *

buffer = b"wYHASK58kvbMpi6GmwnmZW19JIRKqqmp"

length = 32

op = bytearray(buffer)

op = op[:length]

for i in range(length):
    op[i] = ((op[i] ^ 0xcc) - i) & 0xFF


payload = bytes(op)

print(payload)

