#!/usr/bin/env python3
import struct

magic = b"cIMG"
version = 2
width = 2
height = 2

pixels = [
    (119, 170, 30, ord('c')),
    (195,  26,  8, ord('I')),
    (102,  67, 59, ord('M')),
    (176,  91,137, ord('G')),
]

header = struct.pack("<4sHBB", magic, version, width, height)

pixel_bytes = bytearray()
for r,g,b,a in pixels:
    pixel_bytes += struct.pack("<BBBB", r,g,b,a)

with open("file.cimg", "wb") as f:
    f.write(header)
    f.write(pixel_bytes)

