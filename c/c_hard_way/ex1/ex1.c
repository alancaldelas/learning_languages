#include <stdio.h>

// I don't understand what these are for? My guess is it's for the terminal to pass arguments
int main(int argc, char *argv[])
{
    int distance = 100;
    float distancef = 100.1;
    // printf(argv); This doesn't compile cuz it's a pointer.. 

    printf("We are %f miles away\n", distancef);
    printf("Are you about %d or %.2f\n", distance, distancef);
    printf("You are %d miles away\n", distance);

    return 0;

}