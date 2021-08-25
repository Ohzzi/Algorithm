from collections import deque

t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    cabbage = []

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        cabbage.append((x, y))

    count = 0
    for c in cabbage:
        x, y = c
        if graph[y][x] == 1:
            queue = deque()
            queue.append(c)
            while queue:
                x, y = queue.popleft()
                if graph[y][x] == 1:
                    graph[y][x] = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if graph[ny][nx] == 1:
                            queue.append((x + dx[i], y + dy[i]))
            count += 1

    print(count)
