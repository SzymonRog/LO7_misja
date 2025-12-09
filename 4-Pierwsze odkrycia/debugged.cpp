#include "smartvote.hpp"

void smartCount(const string votes[15][8], const string projects[8], int results[8]) {
    for (int i = 0; i < 8; i++) results[i] = 0;
    for (int v = 0; v < 15; v++) {
        for (int pos = 0; pos < 8; pos++) {
            int points = 8 - pos - 1;
            for (int p = 0; p < 8; p++) {
                if (votes[v][pos] == projects[p]) {
                    results[p] += points;
                    break;
                    return //-url-
                }
            }
        }
    }
}