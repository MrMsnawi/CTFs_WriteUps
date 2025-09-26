#!/usr/bin/env python3

header = b"cIMG"
version = b"\x02\x00"
width = 41
w = width.to_bytes(2, byteorder='little')
height = 22
h = height.to_bytes(2, byteorder='little')
d1 = b"\x21" * 902
r, g, b = 0x8C, 0x1D, 0x40
ascii_c = ord("A")

size = 902 * 4
d2 = bytearray()
for _ in range (size):
    d2 += bytes([r, g, b, ascii_c])

with open("file.cimg", "wb") as file:
    file.write(header + version + w + h)
    file.write(d2)
