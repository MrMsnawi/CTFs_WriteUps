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
    for (int i = 0; i < n - 1; i += 1) {
        unsigned short *chunk = (unsigned short*)(buffer + i);
        *chunk += i * 7;
        *chunk = *chunk ^ 16963;
        *chunk = (*chunk << 8) | ((*chunk >> 8) & 0xff);
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
    printf("the key : %s\n", key);
    if (!memcmp(key, "L3sVRSZdP6vGWRJE4bGp3IRJ4rPJMV2y", 32)) {
        printf("Good job! Go get your flag.\n");
        show_flag();
    }
    else {
        printf("Wrong key!\n");
    }
}
