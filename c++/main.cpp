#include <iostream>

int len(char string[]) {

    int i = 0;
    while ( string[i] != '\0'  ) {

        i++;
    }

    return i;
}

int main() {

    char nome[] = "ivan";
    std::cout << len(nome);
    return 0;
}
