# CrackMe Writeup: Beginner Challenge (kropesiunia)

**Platform:** crackmes.one | **Difficulty:** 1 | **Arch:** x86-64 Windows (PE) | **Language:** C++ (Debug build)

---

## Recon

```
$ file crackme.exe
PE32+ executable (console) x86-64, for MS Windows
```

Binary was compiled in Visual Studio **Debug mode** (requires `MSVCP140D.dll`, `ucrtbased.dll`). Could not run under Wine — solved via static analysis only.

Running `strings` immediately reveals the password:

```
letmein
Please enter the password: 
Access granted!
Access denied!
```

## Ghidra Confirmation

The `passwordCheck` function stores `"letmein"` in a local string, reads user input, and compares them:

```c
thunk_FUN_1400155e0(local_130, "letmein");       // expected password
thunk_FUN_14001d6c0(cin_exref, local_170);        // read user input
cVar1 = thunk_FUN_1400139c0(local_170, local_130); // string compare
if (cVar1 == '\0')
    // "Access denied!"
else
    // "Access granted!"
```

Plaintext comparison, no hashing or obfuscation.

**Password:** `letmein`

## Tools Used

`strings`, Ghidra (static analysis)