
#define ERROR           #C0392B
#define WARNING         #F39C2D
#define INFORMATION     #57D728
#define DEBUG           #9B59B6
#define SPONSOR         #42A185
#define STACKOVERFLOW   #2980B9
#define DOCUMENTATION   #EC87BF


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
        int r = 0;
        int g = 0;
        int b = 0;
        std::cout << "\033[48;2;" << r << ";" << g << ";" << b << "m";
}

void fg_rgb (int r, int g, int b) {
        std::cout << "\033[38;2;" << r << ";" << g << ";" << b << "m";
}

bool check (char* hex) {
        if (hex[0] == '#') {
                return true;
        }
        else 
                return false;
}

int parse (char* hex) {
        
        if(check(hex)) {

        }


}


