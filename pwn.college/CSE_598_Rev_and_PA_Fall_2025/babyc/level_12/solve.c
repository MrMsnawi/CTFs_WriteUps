#include <stdio.h>
#include <string.h>

int main()
{
	char dec[] = "fmEhVDZyKjtijiytg1AThJiKpW0XwR7u";

	unsigned char key = dec[0];
	printf("%c", dec[0]);
	for (int i = 1; i < 32; ++i)
	{
		dec[i] ^= key;
		printf("%c", dec[i]);
	}
}
