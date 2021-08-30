from collections import deque

m, n, h = map(int, input().split())
graph = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

answer = 0
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))


# bfs 함수를 따로 분리하지 않으면 시간 초과가 발생
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for idx in range(6):
            nz = z + dz[idx]
            ny = y + dy[idx]
            nx = x + dx[idx]
            if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))


bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            elif answer < graph[i][j][k]:
                answer = graph[i][j][k]
print(answer - 1)
