#include <iostream>
#include <cstdio>

int len(char string[]) {

    int i = 0;
    while ( string[i] != '\0'  ) {

        i++;
    }

    return i;
}

void bg_rgb(int r, int g, int b)
{
    printf("\u001b[48;2;" << r << ";" << g << ";" << b << "m");
}

int main() {

    bg_rgb(255, 255, 255);
    return 0;
}



/*def bg_rgb(r, g, b):
    return f"\u001b[48;2;{r};{g};{b}m"
def fg_rgb(r, g, b):
    return f"\u001b[38;2;{r};{g};{b}m"

*/
