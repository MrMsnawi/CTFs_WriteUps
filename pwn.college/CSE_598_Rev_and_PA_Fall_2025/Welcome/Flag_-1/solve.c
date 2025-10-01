#include <stdio.h>

int main()
{
	char flag[32] = "ixbhwewqlpfueo8l5mzbes0zoyycbmnd";
	for (int i = 0 ; i < 32 ; i++)
	{
		if (i % 2 == 0)
			flag[i] ^= 0x1;
		else
			flag[i] -= 0x1;
	}
	printf("%s\n", flag);
}

