#include "iostream"
#include <fstream>
#include <string>

// Coming Soon!

int main(int argc, char** argv){
    std::ifstream input(argv[1]);
    std::string line;
    unsigned long i = 0;
    while (std::getline(input, line)) {
        std::cout << line << "\n \n";
    }
}