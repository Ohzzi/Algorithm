n, m = map(int, input().split())

min_num = []
for i in range(n):
    min_num.append(min(list(map(int, input().split()))))

print(max(min_num))
