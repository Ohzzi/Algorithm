n = int(input())

for _ in range(n):
    ox = input()
    score = 1
    total = 0
    for s in ox:
        if s == "X":
            score = 1
        else:
            total += score
            score += 1
    print(total)
