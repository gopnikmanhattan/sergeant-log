
#define ERROR dddddd
#define WARNING #dddddd
#define INFORMATION #000000
#define DEBUG #000000
#define SPONSOR #000000
#define STACKOVERFLOW #000000
#define DOCUMENTATION #000000
#define DATEBG #000000


#include <iostream>

int len (char* word) {
        int i = 0;
        while (word[i] != '\0') {
                i++;
        }
        return i;
}

void bg_rgb (char* color) {
        int rgb;
        rgb = parse(color);
        std::cout << "\033[48;2;" << r << ";" << g << ";" << b << "m";
}

void fg_rgb (int r, int g, int b) {
        std::cout << "\033[38;2;" << r << ";" << g << ";" << b << "m";
}

bool check (char* hex) {
        if (char[0] == '#') {
                return true;
        }
        else 
                return false;
}

int parse (const char[] hex) {
        
        if(check(hex)) {

        }


}


