l = int(input())
s = input()
r = 1
m = 1234567891

hash = 0
for idx, value in enumerate(s):
    hash = (hash + (ord(value) - 96) * r) % m
    r = (r * 31) % m
print(hash % m)
