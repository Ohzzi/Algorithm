import math


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(math.sqrt(num)) == math.sqrt(num):
            answer -= num
        else:
            answer += num
    return answer
