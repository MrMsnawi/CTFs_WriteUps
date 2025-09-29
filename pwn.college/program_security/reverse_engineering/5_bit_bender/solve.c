#include <stdio.h>
#include <string.h>

int main()
{
	char enc[16];
	char res[16];
	char print[17];
	char swaped;

	strncpy(enc, "VLFDYyhuaVqbRBTY", 16);
	for (int i = 0; i < 16; i++)
	{
		swaped = (enc[i] << 4) | (enc[i] >> 4);
		res[i] = swaped - 123;
		print[i] = res[i];
	}
	print[16] = '\0';
	printf("%s", print);
}
