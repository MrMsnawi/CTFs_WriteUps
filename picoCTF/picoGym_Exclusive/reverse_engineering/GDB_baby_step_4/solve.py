#!/usr/bin/env python3

# this from gdb
"""
gdb ./debugger0_d 
GNU gdb (Ubuntu 15.0.50.20240403-0ubuntu1) 15.0.50.20240403-git
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./debugger0_d...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Downloading separate debug info for /home/ousen/Desktop/CTFs_WriteUps/picoCTF/reverse_engineering/picoGym_Exclusive/GDB_baby_step_4/debugger0_d
(No debugging symbols found in ./debugger0_d)                                                                                          
(gdb) set disassembly-flavor intel
(gdb) disas main
Dump of assembler code for function main:
   0x000000000040111c <+0>:	endbr64
   0x0000000000401120 <+4>:	push   rbp
   0x0000000000401121 <+5>:	mov    rbp,rsp
   0x0000000000401124 <+8>:	sub    rsp,0x20
   0x0000000000401128 <+12>:	mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:	mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:	mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:	mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:	mov    edi,eax
   0x0000000000401142 <+38>:	call   0x401106 <func1>
   0x0000000000401147 <+43>:	mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:	leave
   0x000000000040114e <+50>:	ret
End of assembler dump.
(gdb) disas func1
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   rbp
   0x000000000040110b <+5>:	mov    rbp,rsp
   0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:	imul   eax,eax,0x3269
   0x000000000040111a <+20>:	pop    rbp
   0x000000000040111b <+21>:	ret
End of assembler dump.
(gdb) 
"""
a = 0x3269
print(f"picoCTF{{{a}}}")
