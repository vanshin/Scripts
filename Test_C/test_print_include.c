#include <stdio.h>
#include <memory.h>
#include <stdlib.h>

#define MAXLINE 1024
void process_line(const char *filename);

main()
{
    process_line("stdio.h");
}

void process_line(const char *filename)
{
    char *buf,*fName, *match, *subfile;
    fName = (char *)malloc(sizeof(char)*MAXLINE);
    buf = (char *)malloc(sizeof(char)*MAXLINE);
    match = (char *)malloc(sizeof(char)*MAXLINE);
    subfile = (char *)malloc(sizeof(char)*MAXLINE);

    memset(fName,'\0',MAXLINE);
    memset(buf,'\0',MAXLINE);
    memset(match,'\0',MAXLINE);
    memset(subfile,'\0',MAXLINE);

    strcpy(match, "#include");
    strcpy(fName, "C:\\MinGM\\include\\");
    strcat(fName, filename);
    FILE *f;
    f = fopen(fName, "r");
    while (fgets(buf, MAXLINE, f) != NULL)
    {
        if(strstr(buf, match) != NULL)
        {
            strncpy(subfile, strstr(buf,"<")+1, strstr(buf,">")-strstr(buf,"<")-1);
            printf("subfile = %s\n", subfile);
            sleep(3);
            process_line(subfile);
            memset(subfile,'\0',MAXLINE);
        }
        // printf("%s\n", buf);
        memset(buf, '\0', MAXLINE);
    }
}