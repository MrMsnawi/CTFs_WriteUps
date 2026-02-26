# NoraCodes crackme01 — Writeup (No Source Code Peeking)

## Goal
Find the correct input for the binary:

```bash
./crackme01.64
```

## Initial black-box testing
Running with no argument:

```bash
./crackme01.64
Need exactly one argument.
```

So the program requires exactly one input argument.

Running with a wrong guess:

```bash
./crackme01.64 fsdf
No, fsdf is not correct.
```

So it validates the argument against some hidden expected value.

## Dynamic analysis with ltrace
Use `ltrace` to observe libc calls without reading source:

```bash
ltrace ./crackme01.64 aaaa
strncmp("aaaa", "password1", 9)              = -15
__printf_chk(2, 0x62b998200029, 0x7ffe61a09dcf, 112No, aaaa is not correct.
) = 25
+++ exited (status 1) +++
```

Critical observation:

- The binary calls `strncmp` with:
  - user input: `"aaaa"`
  - hidden reference: `"password1"`
  - compare length: `9`

This directly reveals the target string.

## Verify candidate

```bash
./crackme01.64 password1
Yes, password1 is correct!
```

## Flag / Password

`password1`

## Notes
Because `strncmp(..., 9)` is used, the check compares only the first 9 characters. That means any input beginning with `password1` would also pass (e.g., `password1XYZ`).
