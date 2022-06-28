n = int(input())

words = sorted(list({input() for _ in range(n)}), key = lambda x : (len(x), x))

for word in words:
    print(word)
