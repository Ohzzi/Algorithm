/*
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
*/

#include <iostream>
#include <queue>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);

    int n, k, max = 100001;
    bool visited[100001];
    std::fill(visited, visited + 100001, false);
    std::cin >> n >> k;
    visited[n] = true;
    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(n, 0));
    while (!q.empty()) {
        int position = q.front().first;
        int time = q.front().second;
        q.pop();
        if (position == k) {
            std::cout << time;
            break;
        }
        if (position + 1 < max && !visited[position + 1]) {
            q.push(std::make_pair(position + 1, time + 1));
            visited[position + 1] = true;
        }
        if (position - 1 > -1 && !visited[position - 1]) {
            q.push(std::make_pair(position - 1, time + 1));
            visited[position - 1] = true;
        }
        if (position * 2 < max && !visited[position * 2]) {
            q.push(std::make_pair(position * 2, time + 1));
            visited[position * 2] = true;
        }
    }
    return 0;
}