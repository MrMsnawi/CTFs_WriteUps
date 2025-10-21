#include <stdio.h>
#include <string.h>

int main()
{

	char *buffer = strdup("abcd");

	for (int i = 0; i < 5; i++)
	{
		unsigned char *f = (unsigned char*)(buffer + i);
		printf("%d ", *f);
	}	
}
