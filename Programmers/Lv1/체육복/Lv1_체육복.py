def solution(n, lost, reserve):
    answer = 0
    uniform = [0 for i in range(n)]
    for i in lost:
        uniform[i-1] -= 1
    for i in reserve:
        uniform[i-1] += 1
    for i in range(n):
        if uniform[i] == -1:
            if i > 0 and uniform[i-1] > 0:
                uniform[i-1] -= 1
                uniform[i] += 1
            elif i < n-1 and uniform[i+1] > 0:
                uniform[i+1] -= 1
                uniform[i] += 1
        if uniform[i] > -1:
            answer += 1
    return answer