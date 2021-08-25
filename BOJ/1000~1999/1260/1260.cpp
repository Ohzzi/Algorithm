/*
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
*/

#include <iostream>
#include <stack>
#include <queue>

void dfs(int v, int n, int** graph) {
	std::stack<int> st;
	st.push(v);
	printf("%d ", v + 1);
	bool* check = new bool[n];
	std::fill(check, check + n, false);
	check[v] = true;
	while (!st.empty()) {
		int current = st.top();
		st.pop();
		for (int i = 0; i < n; i++) {
			if (graph[current][i]==1 && !check[i]) {
				printf("%d ", i + 1);
				check[i] = true;
				st.push(current);
				st.push(i);
				break;
			}
		}
	}
}

void bfs(int v, int n, int** graph) {
	bool* check = new bool[n];
	std::fill(check, check + n, false);
	std::queue<int> q;
	q.push(v);
	check[v] = true;
	while (!q.empty()) {
		int current = q.front();
		q.pop();
		printf("%d ", current + 1);
		for (int i = 0; i < n; i++) {
			if (graph[current][i] && !check[i]) {
				q.push(i);
				check[i] = true;
			}
		}
	}
}

int main() {
	int n, m, v;
	scanf("%d %d %d", &n, &m, &v);
	int** graph = new int* [n];
	for (int i = 0; i < n; i++) {
		graph[i] = new int[n];
		for (int j = 0; j < n; j++) {
			graph[i][j] = 0;
		}
	}
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a-1][b-1] = 1;
		graph[b-1][a-1] = 1;
	}
	dfs(v - 1, n, graph);
	printf("\n");
	bfs(v - 1, n, graph);
	return 0;
}