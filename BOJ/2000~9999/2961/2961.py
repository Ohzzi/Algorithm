from itertools import combinations

def calculate_difference(ingredients):
    sour = 1
    bitter = 0
    for s, b in ingredients:
        sour *= s
        bitter += b
    return abs(sour - bitter)

n = int(input())
ingredients = []
differences = []
for _ in range(n):
    ingredients.append(list(map(int, input().split())))

for i in range(n):
    ingredients_combinations = list(combinations(ingredients, i + 1))
    for ingredients_combination in ingredients_combinations:
        differences.append(calculate_difference(ingredients_combination))

print(min(differences))
