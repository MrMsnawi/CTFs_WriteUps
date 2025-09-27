#!/usr/bin/env python3

import struct

magic = b"cIMG"
version = 2
w = 2
h = 2

pixels = [
    (49, 196, 198, ord('c')),
    (92, 167, 123, ord('I')),
    (89, 7, 16, ord('M')),
    (244, 63, 16, ord('G')),
]

header = struct.pack("<4sHBB", magic, version, w, h)

pixels_bytes = bytearray()
for r, g, b, a in pixels:
    pixels_bytes += struct.pack("<BBBB", r, g, b, a)

with open("file.cimg", "wb") as file:
    file.write(header)
    file.write(pixels_bytes)
