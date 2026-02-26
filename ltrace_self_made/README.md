# ltrace Self-Made Crackme (C)

This mini challenge demonstrates a classic beginner reverse-engineering pattern:
a password check implemented with a hardcoded `strcmp`.

## Files

- `crackme.c` — source code
- `crackme` — compiled binary

## How the crackme works

The program:

1. Reads user input from stdin.
2. Compares it against a hardcoded secret using `strcmp`.
3. Prints:
   - `Access granted` if it matches
   - `Access denied` otherwise

Because it calls the libc function `strcmp`, the compared strings can be observed at runtime with `ltrace`.

## Build

```bash
gcc -O0 -fno-stack-protector -o crackme crackme.c
```

## Normal execution

Wrong input:

```bash
printf 'wrongpass\n' | ./crackme
```

Expected output:

```text
Enter password: Access denied
```

Correct input:

```bash
printf 'opensesame123\n' | ./crackme
```

Expected output:

```text
Enter password: Access granted
```

## Crack with ltrace

Run the program through `ltrace` with any wrong password:

```bash
printf 'aaaa\n' | ltrace -s 128 ./crackme
```

Look for the `strcmp` call in the trace:

```text
strcmp("aaaa", "opensesame123") = -14
```

The second argument is the hardcoded secret:

- `opensesame123`

Use it to pass the challenge:

```bash
printf 'opensesame123\n' | ./crackme
```

## Notes

- This is intentionally insecure and meant for learning only.
- Any direct string compare to a static secret is easy to recover with dynamic tracing tools.
