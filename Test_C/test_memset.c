#include <stdio.h>
#include <string.h>

main()
{
    int i = 0;
    int data[3] = {1, 2, 3};
    char string[4] = {'a', 'b', 'c'};
    char str[] = "vanshin";
    char *str2 = "vashin1";
    char c1[]={'I',' ','a','m',' ','h','a','p','p','y'};
    // memset(data, "1", sizeof(data));
    // for (i=0; i<3; i++)
        // printf("%d", data[i]);
        // printf("%c", string[i]);
    // printf("%s", string);
    int i1 = sizeof(string);
    // printf("%d", i1);
    // printf("%s", str);
    char *p;
    p = &str2[0];
    printf("%s", str);
    memset(str, '\2', sizeof(str)-1);
    printf("%s", str);
}