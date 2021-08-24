from collections import deque


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0
queue = deque()
queue.append((x, y))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            # 최단경로를 찾는 문제이므로, 해당 노드가 한 번도 방문하지 않은 경우(1인 경우)에만 가면 된다.
            # bfs니까 가능
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[n-1][m-1])
