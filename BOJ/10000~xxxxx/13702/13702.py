from sys import stdin

n, k = map(int, stdin.readline().split())
kettles = [int(stdin.readline()) for _ in range(n)]
left = 1
right = max(kettles)
answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for kettle in kettles:
        cnt += kettle // mid
    if cnt >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
