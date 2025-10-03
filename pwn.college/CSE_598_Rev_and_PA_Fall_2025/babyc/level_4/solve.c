#include <stdio.h>
#include <unistd.h>

int main()
{
	long long p = (1<<64)-1;
	write(1, &p, sizeof(p));
}
