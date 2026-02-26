#include <stdio.h>

int main()
{
    char data[] = "password1";
    for (int i = 0; i < sizeof(data); i++)
    {
        printf("%c", data[i]-1);
    }
    printf("\n");
}