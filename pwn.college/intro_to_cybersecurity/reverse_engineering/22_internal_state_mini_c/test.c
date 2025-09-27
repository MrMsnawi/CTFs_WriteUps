#include <stdio.h>
#include <string.h>

int main()
{
	union oh
	{
		char c;
		int a;
		char h[20];
		char b[10];
	};
	union oh ah;
	ah.a = 10;
	ah.c = 'h';
	strncpy(ah.b, "asdfghjkl", 9);
	strncpy(ah.h, ";", 1);

	printf("size = %zu\n", sizeof(ah));
	printf("c = %c\na = %d\nb = %s\nh = %s\n", ah.c, ah.a, ah.b, ah.h);
}
