#include <string>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include "smartvote.hpp"
#include <iostream>
using namespace std;

void calculateCorrectResults(const string votes[15][8], const string projects[8], int results[8]) {
    for (int i = 0; i < 8; i++) results[i] = 0;

    for (int v = 0; v < 15; v++) {
        for (int pos = 0; pos < 8; pos++) {
            int points = 8 - pos - 1;
            for (int p = 0; p < 8; p++) {
                if (votes[v][pos] == projects[p]) {
                    results[p] += points;
                    break;
                }
            }
        }
    }
}

void generateRandomVotes(string votes[15][8], const string projects[8]) {
    for (int v = 0; v < 15; v++) {
        for (int i = 0; i < 8; i++) votes[v][i] = projects[i];

        // Fisher-Yates shuffle
        for (int i = 7; i > 0; i--) {
            int j = rand() % (i + 1);
            swap(votes[v][i], votes[v][j]);
        }
    }
}

bool checkResults(const int expected[8], const int results[8]) {
    for (int i = 0; i < 8; i++) {
        if (expected[i] != results[i]) return false;
    }
    return true;
}

string komunikat;


bool test() {
    srand(time(NULL));
    komunikat = "";

    string projects[8] = {
        "Projekt_A", "Projekt_B", "Projekt_C", "Projekt_D",
        "Projekt_E", "Projekt_F", "Projekt_G", "Projekt_H"
    };

    string votes[15][8];
    generateRandomVotes(votes, projects);

    int expected[8];
    calculateCorrectResults(votes, projects, expected);

    int results[8];
    smartCount(votes, projects, results);

    if (checkResults(expected, results)) {
        komunikat = "Brawo!! udało ci się znaleźć błąd. Ale co to za komentaz w kodzie z jakimś linkiem: https://truecomp.vercel.app/ .\n";
        cout << komunikat;
        return true;
    }

    komunikat = "BŁĄD Różnice w wynikach:\n";

    for (int i = 0; i < 8; i++) {
        if (expected[i] != results[i]) {
            komunikat += "- " + projects[i] + ": "
                       + to_string(expected[i]) + " -> "
                       + to_string(results[i]) + " (Różnica "
                       + to_string(results[i] - expected[i]) + ")\n";
        }
    }

    cout << komunikat;
    return false;
}

