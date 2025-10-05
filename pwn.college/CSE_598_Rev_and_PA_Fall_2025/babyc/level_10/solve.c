#include <stdio.h>
#include <string.h>

int main()
{
	char *buf = strdup("00QwxrjOKb7Ri6egWyRnTFTK77t1P9DV");
	if (buf == NULL)
		return (perror("strdup"), 1);
	unsigned int *chunk;
	for (int i = 0; i < 32; i += 4)
	{
		chunk = (unsigned int*)(buf + i);
		*chunk -= i;
		*chunk ^= 2166505724;
	}
	for (int i = 0; i < 32; i++)
		printf("%02x ", buf[i]);
}
