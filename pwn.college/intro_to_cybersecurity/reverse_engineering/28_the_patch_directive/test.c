#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
	char buf[50000];

	int fd = open("file.cimg", O_RDONLY);
	int n = read(fd, buf, 50000);
	printf("%s\n\n\n\ncount = %d\n", buf, n);
}
