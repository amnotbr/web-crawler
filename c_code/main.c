#include <stdio.h>
#include <stdlib.h>

#define WORDLIST_PATH "./assets/words.txt"
#define DOMAIN_EXTENSIONS "./assets/domainextensions.txt"
#define POSSIBLE "possiblesitestxt"

int main()
{
    FILE *fptr;

    fptr = fopen(WORDLIST_PATH, "r"); // open the wordlist path
    

    fclose(fptr);
    return 0;
}