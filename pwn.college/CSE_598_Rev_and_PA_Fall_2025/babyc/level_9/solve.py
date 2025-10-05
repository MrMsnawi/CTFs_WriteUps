#!/usr/bin/env python3

buf = b"Bh4ZP1x0o7s0o8mNhT29zL3hZwAFOgyu"

op = bytearray(buf)

length = 32

op = op[:length]

def rot_nibble(x):
    return ((x << 4) | (x >> 4)) & 0xFF

for i in range(length):
    tmp = (op[i] + 42)
    tmp ^= 0x22
    tmp = rot_nibble(tmp)
    op[i] = tmp

payload = bytes(op)
print(payload.hex())
