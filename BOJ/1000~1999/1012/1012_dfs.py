import sys
sys.setrecursionlimit(100000)

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    cabbage = []

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        cabbage.append((x, y))

    result = 0
    for x, y in cabbage:
        if dfs(x, y):
            result += 1
    print(result)
