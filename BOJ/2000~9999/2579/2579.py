from sys import stdin

n = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(n)]
dp = []

if n < 3:
    print(sum(stairs))
else:
    dp.append(stairs[0])
    dp.append(stairs[0] + stairs[1])
    dp.append(stairs[2] + max(stairs[0], stairs[1]))
    for i in range(3, n):
        dp.append(stairs[i] + max(dp[i-2], stairs[i-1] + dp[i-3]))
    print(dp[n-1])