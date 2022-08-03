from sys import stdin
from collections import deque

t = int(stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 1:
            graph[y][x] = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if graph[ny][nx] == 1:
                    queue.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    cabages = []
    queue = deque()
    count = 0
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        field[y][x] = 1
        cabages.append((x, y))
    for cabage in cabages:
        queue.clear()
        x, y = cabage
        if field[y][x] == 1:
            bfs(field, cabage)
            count += 1
    print(count)
