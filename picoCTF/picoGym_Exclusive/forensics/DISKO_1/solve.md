```
$ ls
disko-1.dd.gz

$ file disko-1.dd.gz 
disko-1.dd.gz: gzip compressed data, was "disko-1.dd", last modified: Thu May 15 18:48:20 2025, from Unix, original size modulo 2^32 52428800

$ gunzip disko-1.dd.gz 

$file disko-1.dd 
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32, heads 8, sectors 102400 (volumes > 32 MB), FAT (32 bit), sectors/FAT 788, serial number 0x241a4420, unlabeled

$ strings disko-1.dd | grep picoCTF{
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}

$ 
```

