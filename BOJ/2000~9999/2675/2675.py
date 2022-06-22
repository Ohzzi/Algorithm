t = int(input())

for _ in range(t):
    r, s = input().split()
    p = "".join([c * int(r) for c in s])
    print(p)
