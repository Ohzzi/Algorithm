from sys import stdin
from itertools import combinations

while True:
    numbers = list(stdin.readline().split())
    if numbers[0] == '0':
        break
    for c in combinations(numbers[1:], 6):
        print(" ".join(c))
    print()
