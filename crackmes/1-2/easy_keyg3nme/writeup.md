# CrackMe Writeup: easy keyg3nme (ezman)

**Platform:** crackmes.one | **Difficulty:** 1 | **Arch:** x86-64 Linux

---

## Analysis

The decompiled `main` reads an integer via `scanf`, passes it to `validate_key`, and prints success if it returns 1.

```c
bool validate_key(int param_1) {
    return param_1 % 0x4c7 == 0;
}
```

The key just needs to be divisible by `0x4c7` (1223 in decimal). Any multiple works: 0, 1223, 2446, etc.

**Stack canary** (`in_FS_OFFSET + 0x28`) is present but irrelevant — no overflow vector here.

## Solve

```python
i = 1
while i % 0x4c7 != 0:
    i += 1
print(f"The key is: {i}")  # 1223
```

Or simply: any `n * 1223` is a valid key.

## Tools Used

Ghidra (static analysis), Python (keygen)