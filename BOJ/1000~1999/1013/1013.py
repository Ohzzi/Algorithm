import re

t = int(input())
strings = []

for _ in range(t):
    pattern = re.compile('(100+1+|01)+')
    if re.fullmatch(pattern, input()):
        print('YES')
    else:
        print('NO')
