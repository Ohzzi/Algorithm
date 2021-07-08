def solution(a, b):
    answer = 0
    for idx in range(len(a)):
        answer += a[idx] * b[idx]
    return answer

def other_solution(a, b):
    return sum([x*y for x, y in zip(a,b)])