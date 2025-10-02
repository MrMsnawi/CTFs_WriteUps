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

int main()
{
    char key[1024];
    char target_key[] = "CABy91VskJCJJbVMDnqb";

    puts("This module will familiarize you with C and pwn.college.");
    puts("");
    puts("Give me a valid key, and I will send you the flag!");
    puts("");
    printf("Key: ");
    scanf("%20s", key);

    if (!strncmp(key, target_key, strlen(target_key))) {
        printf("Good job! Go get your flag.\n");
        show_flag();
    }
    else {
        printf("Wrong key!\n");
    }
}
