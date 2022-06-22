t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    apart = [i for i in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            apart[j] += apart[j-1]
    print(apart[-1])
