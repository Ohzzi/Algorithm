from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
m = int(stdin.readline())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
checked = []
stack = [1]
while stack:
    current = stack.pop()
    if current not in checked:
        checked.append(current)
    stack.extend([x for x in graph[current] if x not in checked])
print(len(checked) - 1)
