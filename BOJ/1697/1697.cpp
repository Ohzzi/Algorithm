/*
����
�����̴� ������ ���ٲ����� �ϰ� �ִ�. �����̴� ���� �� N(0 �� N �� 100,000)�� �ְ�, ������ �� K(0 �� K �� 100,000)�� �ִ�. 
�����̴� �Ȱų� �����̵��� �� �� �ִ�. ����, �������� ��ġ�� X�� �� �ȴ´ٸ� 1�� �Ŀ� X-1 �Ǵ� X+1�� �̵��ϰ� �ȴ�.
�����̵��� �ϴ� ��쿡�� 1�� �Ŀ� 2*X�� ��ġ�� �̵��ϰ� �ȴ�.
�����̿� ������ ��ġ�� �־����� ��, �����̰� ������ ã�� �� �ִ� ���� ���� �ð��� �� �� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù ��° �ٿ� �����̰� �ִ� ��ġ N�� ������ �ִ� ��ġ K�� �־�����. N�� K�� �����̴�.
���
�����̰� ������ ã�� ���� ���� �ð��� ����Ѵ�.
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