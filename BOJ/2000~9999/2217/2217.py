from sys import stdin

n = int(stdin.readline())
ropes = sorted([int(stdin.readline()) for _ in range(n)])
print(max([ropes[i] * (n - i) for i in range(n)]))
