#include <stdio.h>
int main( )
{

    int n1, n2;
    int *p1, *p2;

    p1 = &n1;
    p2 = &n2;

    printf( "Enter two numbers: ");
    scanf("%d %d", &n1, &n2);
    printf( "\nBefore Swap: %d %d", *p1, *p2);

    p1 = &n2;
    p2 = &n1;
    printf( "\nAfter Swap: %d %d", *p1, *p2);
    return 0;
}
