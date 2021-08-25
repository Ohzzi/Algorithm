/*
�׷����� DFS�� Ž���� ����� BFS�� Ž���� ����� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
��, �湮�� �� �ִ� ������ ���� ���� ��쿡�� ���� ��ȣ�� ���� ���� ���� �湮�ϰ�, �� �̻� �湮�� �� �ִ� ���� ���� ��� �����Ѵ�.
���� ��ȣ�� 1������ N�������̴�.
ù° �ٿ� ������ ���� N(1 �� N �� 1,000), ������ ���� M(1 �� M �� 10,000), Ž���� ������ ������ ��ȣ V�� �־�����.
���� M���� �ٿ��� ������ �����ϴ� �� ������ ��ȣ�� �־�����.
� �� ���� ���̿� ���� ���� ������ ���� �� �ִ�. �Է����� �־����� ������ ������̴�.
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