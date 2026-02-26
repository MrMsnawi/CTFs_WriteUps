# NoraCodes crackme01e Write-up

## Challenge
Binary: `crackme01e.64`

Goal: find the correct single argument.

## Quick behavior check

Running without arguments:

```bash
./crackme01e.64
Need exactly one argument.
```

Running with a wrong argument:

```bash
./crackme01e.64 aaaa
No, aaaa is not correct.
```

## Dynamic analysis with `ltrace`

`ltrace` reveals the password check directly:

```bash
ltrace ./crackme01e.64 aaaa
strncmp("aaaa", "slm!paas.k", 10) = -18
```

So the expected input is clearly:

```text
slm!paas.k
```

## Bash gotcha (`!` history expansion)

Trying this command in Bash with double quotes:

```bash
./crackme01e.64 "slm!paas.k"
```

can fail with:

```text
bash: !paas.k: event not found
```

because `!` is treated as history expansion in interactive shells.

Working options:

```bash
./crackme01e.64 'slm!paas.k'
```

or disable history expansion first:

```bash
set +H
./crackme01e.64 "slm!paas.k"
```

## Successful run

```bash
./crackme01e.64 "slm!paas.k"
Yes, slm!paas.k is correct!
```

## Source confirmation

The source file (`crackme01e.c`) stores:

```c
char* correct = "slm!paas.k";
if (strncmp(argv[1], correct, strlen(correct))) {
    // wrong
}
```

So this crackme is a straightforward plaintext password check.