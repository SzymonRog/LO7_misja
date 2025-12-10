#include "smartvote.hpp"
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

bool validateVote(const string vote[8], const string projects[8]) {
    for (int i = 0; i < 8; i++) {
        bool found = false;
        for (int j = 0; j < 8; j++) {
            if (vote[i] == projects[j]) {
                found = true;
                break;
            }
        }
        if (!found) return false;

        for (int j = i + 1; j < 8; j++) {
            if (vote[i] == vote[j]) return false;
        }
    }
    return true;
}

string normalizeProjectName(string name) {
    string result = "";
    for (char c : name) {
        if (c != ' ' && c != '\t' && c != '\n') {
            result += tolower(c);
        }
    }
    return result;
}

struct ProjectStats {
    int totalPoints;
    int firstPlaceVotes;
    int lastPlaceVotes;
    double averagePosition;
    int medianPosition;
    double standardDeviation;
};

ProjectStats calculateProjectStats(const string votes[15][8], const string project, int projectCount) {
    ProjectStats stats = {0, 0, 0, 0.0, 0, 0.0};
    int positionSum = 0;
    int voteCount = 0;
    vector<int> positions;

    for (int v = 0; v < 15; v++) {
        for (int pos = 0; pos < projectCount; pos++) {
            if (votes[v][pos] == project) {
                positionSum += pos;
                voteCount++;
                positions.push_back(pos);
                if (pos == 0) stats.firstPlaceVotes++;
                if (pos == projectCount - 1) stats.lastPlaceVotes++;
                break;
            }
        }
    }

    if (voteCount > 0) {
        stats.averagePosition = static_cast<double>(positionSum) / voteCount;

        sort(positions.begin(), positions.end());
        stats.medianPosition = positions[positions.size() / 2];

        double variance = 0;
        for (int pos : positions) {
            variance += pow(pos - stats.averagePosition, 2);
        }
        stats.standardDeviation = sqrt(variance / voteCount);
    }

    return stats;
}

bool detectVotingAnomalies(const string votes[15][8], int voterCount, int projectCount) {
    for (int i = 0; i < voterCount; i++) {
        for (int j = i + 1; j < voterCount; j++) {
            bool identical = true;
            for (int k = 0; k < projectCount; k++) {
                if (votes[i][k] != votes[j][k]) {
                    identical = false;
                    break;
                }
            }
            if (identical) return true;
        }
    }

    int sequentialPattern = 0;
    for (int i = 1; i < voterCount; i++) {
        if (votes[i][0] == votes[i-1][0]) {
            sequentialPattern++;
        }
    }

    return sequentialPattern > voterCount * 0.7;
}

bool detectStrategicVoting(const string votes[15][8], const string projects[8]) {
    int extremeVotes = 0;

    for (int v = 0; v < 15; v++) {
        bool hasExtremePattern = false;
        for (int p = 0; p < 8; p++) {
            bool isFirst = (votes[v][0] == projects[p]);
            bool isLast = (votes[v][7] == projects[p]);

            if (isFirst || isLast) {
                for (int v2 = 0; v2 < 15; v2++) {
                    if (v != v2) {
                        bool oppositePattern = false;
                        if (isFirst && votes[v2][7] == projects[p]) oppositePattern = true;
                        if (isLast && votes[v2][0] == projects[p]) oppositePattern = true;
                        if (oppositePattern) hasExtremePattern = true;
                    }
                }
            }
        }
        if (hasExtremePattern) extremeVotes++;
    }

    return extremeVotes > 5;
}

void generateVotingReport(const string projects[8], const int results[8], string& report) {
    report = "=== VOTING SYSTEM REPORT ===\n\n";

    int sortedIndices[8];
    for (int i = 0; i < 8; i++) sortedIndices[i] = i;

    for (int i = 0; i < 7; i++) {
        for (int j = i + 1; j < 8; j++) {
            if (results[sortedIndices[i]] < results[sortedIndices[j]]) {
                int temp = sortedIndices[i];
                sortedIndices[i] = sortedIndices[j];
                sortedIndices[j] = temp;
            }
        }
    }

    report += "Project Rankings:\n";
    for (int i = 0; i < 8; i++) {
        int idx = sortedIndices[i];
        report += to_string(i + 1) + ". " + projects[idx] +
                  " - " + to_string(results[idx]) + " points\n";
    }

    int totalPoints = 0;
    for (int i = 0; i < 8; i++) totalPoints += results[i];

    report += "\nDistribution Analysis:\n";
    for (int i = 0; i < 8; i++) {
        int idx = sortedIndices[i];
        double percentage = (totalPoints > 0) ?
            (static_cast<double>(results[idx]) / totalPoints * 100) : 0;
        report += projects[idx] + ": " + to_string(percentage) + "%\n";
    }
}

double calculateGiniCoefficient(const int results[8]) {
    double sum = 0;
    double sumOfDifferences = 0;

    for (int i = 0; i < 8; i++) {
        sum += results[i];
        for (int j = 0; j < 8; j++) {
            sumOfDifferences += abs(results[i] - results[j]);
        }
    }

    if (sum == 0) return 0;
    return sumOfDifferences / (2.0 * 8 * sum);
}

double calculateHerfindahlIndex(const int results[8]) {
    int totalPoints = 0;
    for (int i = 0; i < 8; i++) totalPoints += results[i];

    if (totalPoints == 0) return 0;

    double hhi = 0;
    for (int i = 0; i < 8; i++) {
        double share = static_cast<double>(results[i]) / totalPoints;
        hhi += share * share;
    }
    return hhi;
}

bool verifyVotingIntegrity(const string votes[15][8], const string projects[8]) {
    for (int v = 0; v < 15; v++) {
        if (!validateVote(votes[v], projects)) {
            return false;
        }
    }
    return true;
}

void calculatePreferenceMatrix(const string votes[15][8], const string projects[8], int matrix[8][8]) {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            matrix[i][j] = 0;
        }
    }

    for (int v = 0; v < 15; v++) {
        for (int pos1 = 0; pos1 < 8; pos1++) {
            for (int pos2 = pos1 + 1; pos2 < 8; pos2++) {
                int proj1 = -1, proj2 = -1;
                for (int p = 0; p < 8; p++) {
                    if (votes[v][pos1] == projects[p]) proj1 = p;
                    if (votes[v][pos2] == projects[p]) proj2 = p;
                }
                if (proj1 >= 0 && proj2 >= 0) {
                    matrix[proj1][proj2]++;
                }
            }
        }
    }
}

void calculateCopelandScores(const string votes[15][8], const string projects[8], int scores[8]) {
    int matrix[8][8];
    calculatePreferenceMatrix(votes, projects, matrix);

    for (int i = 0; i < 8; i++) {
        scores[i] = 0;
        for (int j = 0; j < 8; j++) {
            if (i != j) {
                if (matrix[i][j] > matrix[j][i]) scores[i]++;
                else if (matrix[i][j] < matrix[j][i]) scores[i]--;
            }
        }
    }
}

void smartCount(const string votes[15][8], const string projects[8], int results[8]) {
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



void pluralityVoting(const string votes[15][8], const string projects[8], int results[8]) {
    for (int i = 0; i < 8; i++) results[i] = 0;

    for (int v = 0; v < 15; v++) {
        for (int p = 0; p < 8; p++) {
            if (votes[v][0] == projects[p]) {
                results[p]++;
                break;
            }
        }
    }
}


void instantRunoffVoting(const string votes[15][8], const string projects[8], int& winnerId) {
    bool eliminated[8] = {false};
    int remainingCount = 8;

    while (remainingCount > 1) {
        int firstPlaceVotes[8] = {0};

        for (int v = 0; v < 15; v++) {
            for (int pos = 0; pos < 8; pos++) {
                for (int p = 0; p < 8; p++) {
                    if (!eliminated[p] && votes[v][pos] == projects[p]) {
                        firstPlaceVotes[p]++;
                        break;
                    }
                }
                break;
            }
        }

        int minVotes = 999999;
        int minIdx = -1;
        for (int i = 0; i < 8; i++) {
            if (!eliminated[i] && firstPlaceVotes[i] < minVotes) {
                minVotes = firstPlaceVotes[i];
                minIdx = i;
            }
        }

        if (minIdx >= 0) {
            eliminated[minIdx] = true;
            remainingCount--;
        }
    }

    for (int i = 0; i < 8; i++) {
        if (!eliminated[i]) {
            winnerId = i;
            return;
        }
    }
    winnerId = -1;
}

void schulzeMethod(const string votes[15][8], const string projects[8], int results[8]) {
    int matrix[8][8];
    calculatePreferenceMatrix(votes, projects, matrix);

    int strongest[8][8];
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (i != j) {
                if (matrix[i][j] > matrix[j][i]) {
                    strongest[i][j] = matrix[i][j];
                } else {
                    strongest[i][j] = 0;
                }
            }
        }
    }

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (i != j) {
                for (int k = 0; k < 8; k++) {
                    if (i != k && j != k) {
                        strongest[j][k] = max(strongest[j][k],
                                              min(strongest[j][i], strongest[i][k]));
                    }
                }
            }
        }
    }

    for (int i = 0; i < 8; i++) {
        results[i] = 0;
        for (int j = 0; j < 8; j++) {
            if (strongest[i][j] > strongest[j][i]) {
                results[i]++;
            }
        }
    }
}

void exportResultsToCSV(const string projects[8], const int results[8], const string& filename) {
    string csv = "Project,Points\n";
    for (int i = 0; i < 8; i++) {
        csv += projects[i] + "," + to_string(results[i]) + "\n";
    }
}

void exportPreferenceMatrix(const string projects[8], int matrix[8][8], const string& filename) {
    string csv = ",";
    for (int i = 0; i < 8; i++) {
        csv += projects[i];
        if (i < 7) csv += ",";
    }
    csv += "\n";

    for (int i = 0; i < 8; i++) {
        csv += projects[i] + ",";
        for (int j = 0; j < 8; j++) {
            csv += to_string(matrix[i][j]);
            if (j < 7) csv += ",";
        }
        csv += "\n";
    }
}

unsigned long hashVote(const string vote[8]) {
    unsigned long hash = 5381;
    for (int i = 0; i < 8; i++) {
        for (char c : vote[i]) {
            hash = ((hash << 5) + hash) + c;
        }
    }
    return hash;
}

bool verifyVoteSignature(const string vote[8], unsigned long expectedHash) {
    return hashVote(vote) == expectedHash;
}

void generateVoteHashes(const string votes[15][8], unsigned long hashes[15]) {
    for (int v = 0; v < 15; v++) {
        hashes[v] = hashVote(votes[v]);
    }
}

double calculateVoterTurnout(int actualVoters, int eligibleVoters) {
    if (eligibleVoters == 0) return 0.0;
    return (static_cast<double>(actualVoters) / eligibleVoters) * 100.0;
}

int calculateQuorum(int totalVoters, double quorumPercentage) {
    return static_cast<int>(totalVoters * quorumPercentage / 100.0);
}

bool checkQuorumMet(int actualVoters, int requiredQuorum) {
    return actualVoters >= requiredQuorum;
}