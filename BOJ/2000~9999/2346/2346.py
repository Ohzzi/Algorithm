from sys import stdin

n = int(stdin.readline())
balloons = list(map(int, stdin.readline().split()))
bursted = [False] * n
idx = 0
answer = []
for k in range(n):
    bursted[idx] = True
    answer.append(idx + 1)
    diff = balloons[idx]
    while diff != 0 and False in bursted:
        idx += diff // abs(diff)
        if idx == n:
            idx = 0
        elif idx == -1:
            idx = n - 1
        if not bursted[idx]:
            diff -= diff // abs(diff)
print(*answer)
