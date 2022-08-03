n = int(input())
people = list(map(int, input().split()))

people.sort()
time = 0
total_time = 0
for person_time in people:
    time += person_time
    total_time += time
print(total_time)

# print(sum([sum(people[:i+1]) for i in range (n)]))
