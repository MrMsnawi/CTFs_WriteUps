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

void decrypt(char* buffer, size_t n)
{
    for (int i = 0; i < n; i += 4) {
        unsigned int *chunk = (unsigned int*)(buffer + i);
        *chunk = *chunk ^ 2166505724;
        *chunk += i;
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
    read(0, key, 32);
    // Decrypt
    decrypt(key, 32);
    // Do the comparison
    if (!memcmp(key, "00QwxrjOKb7Ri6egWyRnTFTK77t1P9DV", 32)) {
        printf("Good job! Go get your flag.\n");
        show_flag();
    }
    else {
        printf("Wrong key!\n");
    }
}
