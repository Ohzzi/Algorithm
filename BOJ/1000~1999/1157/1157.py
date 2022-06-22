word = input().upper()

counts = dict.fromkeys(set(word), 0)

for c in word:
    counts[c] += 1

maxValues = [k for k,v in counts.items() if max(counts.values()) == v]
if (len(maxValues) == 1):
    print(maxValues[0])
else:
    print("?")
