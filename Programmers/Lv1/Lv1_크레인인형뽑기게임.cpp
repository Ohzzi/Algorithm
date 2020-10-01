#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int n = board[0].size();

    stack<int> stack;

    for (int i = 0; i < moves.size(); i++) {
        for (int j = 0; j < n; j++) {
            int tmp = board[j][moves[i] - 1];
            if (tmp != 0) {
                board[j][moves[i] - 1] = 0;
                if (stack.empty()) {
                    stack.push(tmp);
                }
                else if (tmp == stack.top()) {
                    stack.pop();
                    answer += 2;
                }
                else {
                    stack.push(tmp);
                }
                break;
            }
        }
    }

    return answer;
}