min_num, max_num = map(int, input().split())
sieve = [True for _ in range(max_num - min_num + 1)]
for i in range(2, int(max_num ** 0.5) + 1):
    square = i * i
    quotient = min_num // square
    while True:
        tmp = square * quotient
        quotient += 1
        if tmp < min_num:
            continue
        if tmp > max_num:
            break
        sieve[tmp - min_num] = False
print(sieve.count(True))
