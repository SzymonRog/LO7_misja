#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void bordaCount(const string votes[15][8], const string projects[8], int results[8]) {
    for (int i = 0; i < 8; i++) results[i] = 0;

    for (int v = 0; v < 15; v++) {
        for (int pos = 0; pos < 8; pos++) {
            int points = 8 - pos - 1; // 4,3,2,1,0

            for (int p = 0; p < 8; p++) {
                if (votes[v][pos] == projects[p]) {
                    results[p] += points;
                    break;
                }
            }
        }
    }
}

int main() {
    ifstream file("tests.txt");
    if (!file) {
        cout << "Nie moge otworzyc tests.txt\n";
        return 1;
    }

    string tag;
    int testNum = 1;

    while (file >> tag) {
        if (tag != "TEST") break;

        string projects[8];
        for (int i = 0; i < 8; i++)
            file >> projects[i];

        string votes[15][8];
        for (int v = 0; v < 15; v++)
            for (int p = 0; p < 8; p++)
                file >> votes[v][p];

        int expected[8];
        for (int i = 0; i < 8; i++)
            file >> expected[i];

        string endTag;
        file >> endTag;

        int results[8];
        bordaCount(votes, projects, results);

        bool ok = true;
        for (int i = 0; i < 8; i++)
            if (expected[i] != results[i])
                ok = false;

        cout << "Test " << testNum << ": ";
        if (ok) {
            cout << "OK\n";
        } else {
            cout << "BLAD\n";
            cout << " Oczekiwane: ";
            for (int i = 0; i < 8; i++) cout << expected[i] << " ";
            cout << "\n Otrzymane: ";
            for (int i = 0; i < 8; i++) cout << results[i] << " ";
            cout << "\n";
        }

        testNum++;
    }

    return 0;
}
