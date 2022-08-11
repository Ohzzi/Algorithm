from sys import stdin

graph = [stdin.readline().split() for _ in range(5)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, number):
    number += graph[y][x]
    if len(number) == 6:
        result.append(number)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            dfs(nx, ny, number)

for i in range(5):
    for j in range(5):
        dfs(j, i, "")

print(len(set(result)))