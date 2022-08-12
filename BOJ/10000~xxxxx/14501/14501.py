from sys import stdin

n = int(stdin.readline())
T = []
P = []
dp = [0] * n
for i in range(n):
    t, p = map(int, stdin.readline().split())
    T.append(t)
    P.append(p)

if T[0] - 1 < n:
    dp[T[0] - 1] = P[0]

for i in range(1, n):
    dp[i] = max(dp[:i+1])
    end = i + T[i] - 1
    if end < n:
        dp[end] = max(dp[end], dp[i-1] + P[i])
print(dp[n-1])