#include <stdio.h>

int main()
{
	char buffer[32] = "iYfFJa4X6ExwyitmA2c1w5XMhRR60WHf";

	for (int i = 0; i < 32; i++)
	{
		buffer[i] = buffer[i] - 0xc8;
		printf("%02X ", buffer[i]);
	}
}
