#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void show_flag()
{
    char flag[1024] = {0};
    FILE* fp = fopen("/flag", "rb");
    if (fp == NULL) {
        printf("Cannot open /flag.\n");
        perror("fopen");
        return;
    }
    fread(flag, 1024, 1, fp);
    fclose(fp);
    printf("Your flag: %s\n. Congrats!\n", flag);
}

void decrypt(unsigned char* buffer, size_t n)
{
    for (int i = 0; i < n; ++i) {
        buffer[i] = ((buffer[i] << 4) | (buffer[i] >> 4));
        buffer[i] = buffer[i] ^ 0x22;
        buffer[i] -= 42;
    }
}

int main()
{
    char key[1024] = {0};

    puts("This module will familiarize you with C and pwn.college.");
    puts("");
    puts("Give me a valid key, and I will send you the flag!");
    puts("");
    printf("Key: ");
    fflush(stdout);
    read(0, key, 32);
    // Decrypt
    decrypt((unsigned char*)key, 32);
    // Do the comparison
    if (!memcmp(key, "Bh4ZP1x0o7s0o8mNhT29zL3hZwAFOgyu", 32)) {
        printf("Good job! Go get your flag.\n");
        show_flag();
    }
    else {
        printf("Wrong key!\n");
    }
}
