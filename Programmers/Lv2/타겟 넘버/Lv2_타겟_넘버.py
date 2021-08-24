from collections import deque


def bfs_solution(numbers, target):
    queue = deque()
    queue.append(0)
    for idx, number in enumerate(numbers):
        for _ in range(2 ** idx):
            in_queue = queue.popleft()
            queue.append(in_queue - number)
            queue.append(in_queue + number)
    return queue.count(target)


def dfs_solution(numbers, target):
    stack = []
    answer = 0
    stack.append((0, -1))
    while stack:
        (temp, level) = stack.pop()
        level += 1
        if level < len(numbers):
            stack.append((temp - numbers[level], level))
            stack.append((temp + numbers[level], level))
        else:
            if temp == target:
                answer += 1
    return answer
