#include <string>
#include <vector>
#include <cctype>

using namespace std;

bool solution(string s) {
    bool answer = true;
    int length = s.length();
    if (length != 4 && length != 6) {
        return false;
    }
    for (int i = 0; i < length; i++) {
        if (!isdigit(s[i])) {
            return false;
        }
    }

    return answer;
}