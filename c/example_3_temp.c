#include <stdio.h>

main () {

    /* this is a comment */
    int cel, fahr, lower, upper, step;
    printf("Hello");

    lower = 0; /* Limit on where we start */
    upper = 300; // Upper limit
    step = 20; // how we jump

    fahr=lower;

    while (fahr <= upper) {
        cel = 5 * (fahr - 32) /9;
        printf("%d\t%d\n", fahr, cel);
        fahr = fahr + step;

    }

}