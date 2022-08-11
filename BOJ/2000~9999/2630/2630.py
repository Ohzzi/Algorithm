from sys import stdin

def check_white(graph, y, x, size):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] == 1:
                return False
    return True

def check_blue(graph, y, x, size):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] == 0:
                return False
    return True

def count_white(paper, y, x, size):
    if size == 0:
        return 0
    if check_white(paper, y, x, size):
        return 1
    ny1, ny2 = y, y + size // 2
    nx1, nx2 = x, x + size // 2
    return count_white(paper, ny1, nx1, size // 2) + count_white(paper, ny1, nx2, size // 2) + count_white(paper, ny2, nx1, size // 2) + count_white(paper, ny2, nx2, size // 2)

def count_blue(paper, y, x, size):
    if size == 0:
        return 0
    if check_blue(paper, y, x, size):
        return 1
    ny1, ny2 = y, y + size // 2
    nx1, nx2 = x, x + size // 2
    return count_blue(paper, ny1, nx1, size // 2) + count_blue(paper, ny1, nx2, size // 2) + count_blue(paper, ny2, nx1, size // 2) + count_blue(paper, ny2, nx2, size // 2)

n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
print(count_white(paper, 0, 0, n))
print(count_blue(paper, 0, 0, n))
