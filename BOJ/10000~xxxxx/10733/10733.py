k = int(input())

numbers = []
for _ in range(k):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))
