#include <stdio.h>

main()
{
    int i = 0;
    int data[3] = {1, 2, 3};
    char string[3] = {"a", "b", "c"};
    char str[] = "vanshin";
    // memset(data, "1", sizeof(data));
    for (i=0; i<3; i++)
        printf("%d", data[i]);
        printf("%c", string[i]);
    printf("%s", str);
}