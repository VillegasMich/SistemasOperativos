#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  printf("hello (pid:%d)\n", (int)getpid());
  int rc = fork();
  if (rc < 0) {
    fprintf(stderr, "fork failed\n");
    exit(1);
  } else if (rc == 0) { // CHILD
    printf("child (pid:%d)\n", (int)getpid());
    printf("child write success\n");
    close(STDOUT_FILENO);
    open("./cap5ProcessAPI.output", O_CREAT | O_WRONLY | O_TRUNC, S_IRWXU);
    char *myargs[3];
    myargs[0] = strdup("wc");
    myargs[1] = strdup("cap5ProcessAPI.c");
    myargs[2] = NULL;
    execvp(myargs[0], myargs);
    printf("this shouldn’t print out");
  } else {
    int rc_wait = wait(NULL);
    printf("parent of %d (rc_wait:%d) (pid:%d)\n", rc, rc_wait, (int)getpid());
  }
  return 0;
}
