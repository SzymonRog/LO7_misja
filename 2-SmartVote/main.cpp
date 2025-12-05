#include <iostream>
#include <string>
#include "smartvote.hpp"


using namespace std;


int main() {
const int projnum = 8;
const int votenum = 15;


string projects[projnum] = {
"Projekt_A", "Projekt_B", "Projekt_C", "Projekt_D",
"Projekt_E", "Projekt_F", "Projekt_G", "Projekt_H"
};


string votes[votenum][projnum] = {
{"Projekt_A", "Projekt_B", "Projekt_C", "Projekt_D", "Projekt_E", "Projekt_F", "Projekt_G", "Projekt_H"},
{"Projekt_B", "Projekt_C", "Projekt_A", "Projekt_D", "Projekt_E", "Projekt_H", "Projekt_G", "Projekt_F"},
{"Projekt_C", "Projekt_A", "Projekt_B", "Projekt_E", "Projekt_D", "Projekt_F", "Projekt_H", "Projekt_G"},
{"Projekt_D", "Projekt_B", "Projekt_C", "Projekt_A", "Projekt_E", "Projekt_G", "Projekt_F", "Projekt_H"},
{"Projekt_E", "Projekt_A", "Projekt_B", "Projekt_C", "Projekt_D", "Projekt_H", "Projekt_F", "Projekt_G"},
{"Projekt_F", "Projekt_B", "Projekt_C", "Projekt_A", "Projekt_D", "Projekt_E", "Projekt_H", "Projekt_G"},
{"Projekt_G", "Projekt_A", "Projekt_D", "Projekt_C", "Projekt_B", "Projekt_E", "Projekt_F", "Projekt_H"},
{"Projekt_H", "Projekt_B", "Projekt_A", "Projekt_C", "Projekt_D", "Projekt_E", "Projekt_F", "Projekt_G"},
{"Projekt_A", "Projekt_C", "Projekt_B", "Projekt_D", "Projekt_E", "Projekt_F", "Projekt_H", "Projekt_G"},
{"Projekt_B", "Projekt_A", "Projekt_C", "Projekt_D", "Projekt_E", "Projekt_H", "Projekt_F", "Projekt_G"},
{"Projekt_C", "Projekt_B", "Projekt_A", "Projekt_E", "Projekt_D", "Projekt_F", "Projekt_G", "Projekt_H"},
{"Projekt_D", "Projekt_C", "Projekt_B", "Projekt_A", "Projekt_E", "Projekt_F", "Projekt_G", "Projekt_H"},
{"Projekt_E", "Projekt_D", "Projekt_C", "Projekt_B", "Projekt_A", "Projekt_F", "Projekt_H", "Projekt_G"},
{"Projekt_F", "Projekt_E", "Projekt_D", "Projekt_C", "Projekt_B", "Projekt_A", "Projekt_H", "Projekt_G"},
{"Projekt_G", "Projekt_H", "Projekt_A", "Projekt_B", "Projekt_C", "Projekt_D", "Projekt_E", "Projekt_F"}
};
int results[projnum] = {0};


smartCount(votes, projects, results);


cout << "Wyniki glosowania metoda Borda:\n";
for (int i = 0; i < projnum; i++) {
cout << projects[i] << ": " << results[i] << " punktów\n";
}


return 0;
}