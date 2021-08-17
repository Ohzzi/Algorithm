n = int(input())
x, y = 1, 1
move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

command = input().split()
for c in command:
    x += move[c][0]
    y += move[c][1]
    if x > n or x < 1 or y > n or y < 1:
        x -= move[c][0]
        y -= move[c][1]

print(x, y)
