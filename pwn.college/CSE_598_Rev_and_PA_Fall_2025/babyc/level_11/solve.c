#include <stdio.h>
#include <string.h>

int main()
{
	char *buf = strdup("L3sVRSZdP6vGWRJE4bGp3IRJ4rPJMV2y");
	if (buf == NULL)
		return (perror("strdup"), 1);
	//unsigned short *chunk;
	for (int i = 30; i >= 0; i--)
	{
		unsigned short *chunk = (unsigned short*)(buf + i);
		unsigned short v = ((*chunk << 8) | (*chunk >> 8));
		v ^= 16963;
		v -= i * 7;
		chunk[0] = v;
		
	}
	for (int i = 0; i < 32; i++)
		printf("%c", buf[i]);
}
