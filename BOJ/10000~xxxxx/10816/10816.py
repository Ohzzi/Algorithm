from collections import defaultdict

n = int(input())
numbers = defaultdict(int)
for number in list(map(int, input().split())):
    numbers[number] += 1
m = int(input())
targets = [str(numbers[target]) for target in list(map(int, input().split()))]
print(" ".join(targets))
