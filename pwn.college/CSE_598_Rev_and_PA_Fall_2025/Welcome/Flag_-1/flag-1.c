#include <stdio.h>
#include <string.h>

int check_flag(char* flag)
{
  for (int i = 0; i < 32; i++) {
    if (i % 2 == 0) {
      flag[i] ^= 0x1;
    } else {
      flag[i] += 0x1;
    }
  }
  if (!memcmp(flag, "ixbhwewqlpfueo8l5mzbes0zoyycbmnd", 32)) {
      return 0;
  }
  return 1;
}


int main(int argc, char** argv)
{
  char flag[1024] = {0};
  printf("%s\nInput flag: ", argv[0]);
  scanf("%1023s", flag);
  if (!check_flag(flag)) {
    puts("Congrats!");
    // open the flag file and read it
    FILE* f = fopen("/flag", "rb");
    if (f) {
      char buf[1024];
      fread(buf, 1, sizeof(buf)-1, f);
      buf[sizeof(buf)-1] = 0;
      puts(buf);
      fclose(f);
    } else {
      puts("Unexpected: Flag file not found.");
      return 1;
    }
  } else {
    puts("Wrong flag :<");
  }
}
