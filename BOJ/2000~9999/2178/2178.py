from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for n in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])
