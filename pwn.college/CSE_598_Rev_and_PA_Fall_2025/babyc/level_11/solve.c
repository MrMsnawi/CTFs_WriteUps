#include <stdio.h>
#include <string.h>

int main()
{
	char *buf = strdup("L3sVRSZdP6vGWRJE4bGp3IRJ4rPJMV2y");
	if (buf == NULL)
		return (perror("strdup"), 1);
	unsigned short *chunk;
	for (int i = 30; i >= 0; i--)
	{
		chunk = (unsigned short*)(buf + i);
		//*chunk = ((*chunk << 8) | (*chunk >> 8));
		*chunk ^= 16963;
		*chunk -= i * 7;
		*chunk = ((*chunk << 8) | (*chunk >> 8));
	}
	for (int i = 0; i < 32; i++)
		printf("%02x ", buf[i]);
}
