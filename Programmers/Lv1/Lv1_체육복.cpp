#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int* uniform = new int[n + 1];
    fill(uniform, uniform + n + 1, 0);
    for (int i = 0; i < reserve.size(); i++) {
        uniform[reserve[i]]++;
    }
    for (int i = 0; i < lost.size(); i++) {
        uniform[lost[i]]--;
    }
    for (int i = 1; i < n + 1; i++) {
        if (uniform[i] == -1) {
            if (i > 1 && uniform[i - 1] == 1) {
                uniform[i - 1]--;
                uniform[i] = 0;
            }
            else if (i < n && uniform[i + 1] == 1) {
                uniform[i + 1]--;
                uniform[i] = 0;
            }
        }
        if (uniform[i] >= 0) {
            answer++;
        }
    }
    return answer;
}