#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

char* sha256sum(char* string)
{
    unsigned char digest[32] = {0};
    char* digest_str = malloc(65);
    memset(digest_str, 0, 33);
    MD5((unsigned char*)string, strlen(string), digest);

    for (int i = 0; i < 32; ++i)
    {
        sprintf(digest_str + i * 2, "%02x", digest[i]);
    }

    return digest_str;
}


int check_flag(char* flag)
{
    char* checksum = sha256sum(flag);
    if (!memcmp(checksum, "7bf46ad61adc2265f803fc3b798b3559ffc92c458b8c2fae185c283126663580", 32)) {
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
