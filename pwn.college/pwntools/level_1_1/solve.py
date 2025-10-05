#!/usr/bin/env python3

from pwn import *
from struct import pack

program = "./pwntools-tutorials-level1.1"

p = process(program)

b1 = b'p'
b2 = b'\x15'

p1 = b1[0]
p2 = b2[0]

p3 = 123456789
#p3_b = p3.to_bytes(4, byteorder='little')
p4 = b"Bypass Me:)"

payload = bytearray()
payload = struct.pack("<BBi11s", p1, p2, p3, p4)
payload += b'\n'

p.sendafter(b":)\n###\n", payload)

flag = p.recvline()

print(f"flag is : {flag}")
