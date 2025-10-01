#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

char* md5sum(char* string)
{
    unsigned char digest[16] = {0};
    char* digest_str = malloc(33);
    memset(digest_str, 0, 33);
    MD5((unsigned char*)string, strlen(string), digest);

    for (int i = 0; i < 16; ++i)
    {
        sprintf(digest_str + i * 2, "%02x", digest[i]);
    }

    return digest_str;
}


int check_flag(char* flag)
{
    char* checksum = md5sum(flag);
    if (!memcmp(checksum, "7de38f3c3d3baa7ca58a366f09577586", 32)) {
        return 0;
    }
    return 1;
}


int main(int argc, char** argv)
{
    char flag[1024];
    printf("%s\nInput flag: ", argv[0]);
    scanf("%s", flag);
    if (!check_flag(flag)) {
        puts("Congrats!");
        // open the flag file and read it
        FILE* f = fopen("/flag", "rb");
        if (f) {
            char buf[1024];
            fread(buf, 1, sizeof(buf)-1, f);
            buf[sizeof(buf)-1] = 0;
            puts(buf);
            fclose(f);
        } else {
            puts("Unexpected: Flag file not found.");
            return 1;
        }
    } else {
        puts("Wrong flag :<");
    }
}
