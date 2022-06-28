def count(board, x_start, y_start):
    BW_count = 0
    WB_count = 0
    for i in range(8):
        for j in range(8):
            if board[y_start + i][x_start + j] != BW[i][j]:
                BW_count += 1
            if board[y_start + i][x_start + j] != WB[i][j]:
                WB_count += 1
    return BW_count if BW_count < WB_count else WB_count
    
n, m = map(int, input().split())

BW = [['B','W'] * 4, ['W','B'] * 4] * 4
WB = [['W','B'] * 4, ['B','W'] * 4] * 4

board = [input() for _ in range(n)]
min_cnt = 2500
for y in range(n - 7):
    for x in range(m - 7):
        cnt = count(board, x, y)
        min_cnt = cnt if cnt < min_cnt else min_cnt
print(min_cnt)
