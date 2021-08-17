location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1
move = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
cnt = 0

for m in move:
    if 0 < row + m[0] <= 8 and 0 < col + m[1] <= 8:
        cnt += 1

print(cnt)
