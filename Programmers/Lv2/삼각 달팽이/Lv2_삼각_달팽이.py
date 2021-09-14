def solution(n):
    answer = [[0 for _ in range(i+1)] for i in range(n)]
    x = 0
    y = -1
    number = 0
    for d in range(n):
        for _ in range(d, n):
            number += 1
            if d % 3 == 0:
                y += 1
            elif d % 3 == 1:
                x += 1
            else:
                x -= 1
                y -= 1
            answer[y][x] = number
    return sum(answer, [])
