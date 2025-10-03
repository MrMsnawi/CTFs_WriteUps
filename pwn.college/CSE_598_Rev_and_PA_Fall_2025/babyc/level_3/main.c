#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

void load_random_key(char* buffer, size_t n)
{
    FILE* fp = fopen("/dev/urandom", "rb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }
    fread(buffer, n, 1, fp);
    fclose(fp);
}

int main()
{
    char key[1024] = {0};
    char target_key[32] = {0};
    puts("This module will familiarize you with C and pwn.college.");
    puts("");
    puts("Give me a valid key, and I will send you the flag!");
    puts("");
    printf("Key: ");
    scanf("%20s", key);
    // Load a random key
    load_random_key(target_key, sizeof(target_key) - 1);
    // Do the comparison
    if (!strncmp(key, target_key, strlen(target_key))) {
        printf("Good job! Go get your flag.\n");
        show_flag();
    }
    else {
        printf("Wrong key!\n");
    }
}
