#!/usr/bin/env python3

magic = b"cIMG"
version = b"\x02\x00\x00\x00"
width = 20
height = 22
w = width.to_bytes(4, byteorder='little')
h = height.to_bytes(4, byteorder='little')

r, g, b = 0x8c, 0x1d, 0x40
ascii_c = ord("A")

size = 20 * 22

pixels = bytearray()
for _ in range(size):
    pixels += bytes([r, g, b, ascii_c])


with open("file.cimg", "wb") as file:
    file.write(magic + version + w + h)
    file.write(pixels)
