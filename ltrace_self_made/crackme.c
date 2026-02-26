#include <stdio.h>
#include <string.h>

int main(void) {
    char input[64];
    const char *secret = "opensesame123";

    printf("Enter password: ");
    if (scanf("%63s", input) != 1) {
        puts("Input error");
        return 1;
    }

    if (strcmp(input, secret) == 0) {
        puts("Access granted");
    } else {
        puts("Access denied");
    }

    return 0;
}
