from sys import stdin

left = list(stdin.readline().strip())
m = int(stdin.readline())
right = []

for _ in range(m):
    command = stdin.readline().strip()
    if command == 'L' and left:
        right.append(left.pop())
    elif command == 'D' and right:
        left.append(right.pop())
    elif command == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[2])
left.extend(reversed(right))
print("".join(left))
