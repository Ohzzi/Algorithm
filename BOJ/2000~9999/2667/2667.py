n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    answer = 0
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y] == 1:
        answer += 1
        for i in range(4):
            graph[x][y] = 0
            nx = x + dx[i]
            ny = y + dy[i]
            answer += dfs(nx, ny)
    return answer


result = []
count = 0
for i in range(n):
    for j in range(n):
        d = dfs(i, j)
        if d > 0:
            count += 1
            result.append(d)
result.sort()

print(count)
for r in result:
    print(r)
