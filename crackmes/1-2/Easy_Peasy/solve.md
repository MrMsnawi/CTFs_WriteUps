# CrackMe Writeup: Easy Peasy (whitecr0w)

**Platform:** crackmes.one | **Difficulty:** 1 | **Arch:** x86-64 Windows (PE) | **Language:** C++

---

## Analysis

Ghidra decompilation shows two hardcoded `std::string` credentials compared via `std::operator==`:

```
Username: iwonderhowitfeelstobeatimetraveler
Password: heyamyspaceboardisbrokencanyouhelpmefindit?
```

No obfuscation, no hashing — plaintext comparison.

## Solution

```
$ wine EasyPeasy.exe
Please, login with your credentials.
Username:iwonderhowitfeelstobeatimetraveler
Now, please insert the password.
Password:heyamyspaceboardisbrokencanyouhelpmefindit?
You have successfully logged into the system.
```

## Tools Used

Ghidra (static analysis), Wine (execution on Linux)