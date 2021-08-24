n, m = map(int, input().split())
graph = []
# n x m 그래프 입력
for _ in range(n):
    graph.append(list(map(int, input())))


# DFS 탐색
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


# 그래프의 모든 부분을 순회하며 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
            # dfs 함수를 호출하면 재귀적으로 계속 dfs를 호출하면서 비어있는 칸(0인 칸)에 음료수를 채우기 때문에(1로 채우기 때문에)
            # 붙어있는 묶음 덩이를 모두 채울 수 있다. 따라서 result 값을 1 올려주면 된다.
print(result)
