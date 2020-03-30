#include "basi.h"
#include <iostream>

int len (char* word) {
	int i = 0;
	while (word[i] != '\0') {
		i++;
	}
	return i;
}

void bg_rgb (int r, int g, int b) {
	std::cout << "\033[48;2;" << r << ";" << g << ";" << b << "m";
}

void fg_rgb (int r, int g, int b) {
	std::cout << "\033[38;2;" << r << ";" << g << ";" << b << "m";
}
