#include <stdio.h>


int main()
{
	char str[] = "tF7x9yWImPX90sRIP8HM25OqYUO5n8YS";
	
	for (int i = 0; i < 32; ++i)
		str[i] = str[i] - 1;
	printf("%s", str);
}
