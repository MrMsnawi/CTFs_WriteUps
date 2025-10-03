#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dlfcn.h>

static FILE *(*my_fopen)(const char *restrict pathname, const char *restrict mode) = NULL;

FILE *fopen(const char *restrict pathname, const char *restrict mode)
{
	if (!my_fopen)
		my_fopen = dlsym(RTLD_NEXT, "fopen");
	if (pathname && strcmp(pathname, "/dev/urandom") == 0)
		return my_fopen("/tmp/fixed_random", mode);
	return my_fopen(pathname, mode);
}

