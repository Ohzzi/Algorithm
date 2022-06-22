from itertools import combinations

n, m = map(int, input().split())
cards = map(int, input().split())

cases = set([sum(c) for c in list(combinations(cards, 3)) if sum(c) <= m])
print(max(cases))
