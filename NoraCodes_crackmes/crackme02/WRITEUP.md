# NoraCodes Crackme02 Writeup

## Challenge
Binary: `crackme02.64`

Goal: find an argument that prints:

`Yes, <input> is correct!`

## Decompiled logic (Ghidra)

From your decompilation:

```c
if (param_1 == 2) {
  input = *(long *)(param_2 + 8);
  character = 'p';
  i = 0;
  do {
    if (*(char *)(input + i) == '\0') break;
    if (character + -1 != (int)*(char *)(input + i)) {
      printf("No, %s is not correct.\n", input);
      return 1;
    }
    character = "password1"[i + 1];
    i = i + 1;
  } while (character != '\0');
  printf("Yes, %s is correct!\n", input);
}
```

This compares each input character against:

- `('p' - 1)` for index 0
- then each next char of `"password1"` minus 1

So the expected transformed string is:

`password1` shifted by `-1` per character.

## Recovering the key

Character-by-character:

- `p -> o`
- `a -> \``
- `s -> r`
- `s -> r`
- `w -> v`
- `o -> n`
- `r -> q`
- `d -> c`
- `1 -> 0`

Result:

`o\`rrvnqc0`

## Verification

```bash
./crackme02.64 "o\`rrvnqc0"
```

Output:

```text
Yes, o`rrvnqc0 is correct!
```

## Notes

- The core check is a static Caesar-like shift (`-1`) over a hardcoded string.
- Because the loop breaks when input ends, **prefixes can also pass** (including empty string). The shown value is the full intended transformed password.
