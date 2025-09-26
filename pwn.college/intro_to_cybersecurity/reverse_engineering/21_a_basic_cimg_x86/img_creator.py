#!/usr/bin/env python3

magic = b"cIMG"
version = b"\x02\x00\x00\x00"
width = 0x3c
w = width.to_bytes(1, byteorder='little')
height = 0x15
h = height.to_bytes(1, byteorder='little')

size = 0x13b0
r, g, b, ascii_c = 0x8c, 0x1d, 0x40, ord("A")

pixels = bytearray()
for _ in range(size):
    pixels += bytes([r, g, b, ascii_c])

with open("file.cimg", "wb") as file:
    file.write(magic + version + w + h)
    file.write(pixels)
