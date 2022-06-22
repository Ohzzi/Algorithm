n = int(input())

num = 1
dif = 0
distance = 1

while num < n:
    dif += 6
    num += dif
    distance += 1

print(distance)
