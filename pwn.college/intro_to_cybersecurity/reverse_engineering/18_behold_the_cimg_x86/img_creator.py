#!/usr/bin/env python3

magic = b"cIMG"
version = b"\x01\x00\x00\x00"
var_15 = 11
var_17 = 25
v1 = var_15.to_bytes(2, byteorder='little')
v2 = var_17.to_bytes(1, byteorder='little')

left = b"a" * 275

with open("file.cimg", "wb") as image:
    image.write(magic + version + v1 + v2 + left)

