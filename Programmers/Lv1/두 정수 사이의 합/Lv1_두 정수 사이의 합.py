def solution(a, b):
    if a == b:
        return a
    elif (a + b) % 2 == 0:
        return ((abs(a-b)+1)//2+0.5) * (a+b)
    else:
        return (abs(a-b)+1)//2 * (a+b)
# 수학적 규칙을 사용해서 억지로 푼 듯한 풀이

def better_solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
# 시간복잡도 O(N)

def better_math_solution(a, b):
    return (abs(a-b)+1) * (a+b) / 2
# 반복을 돌지 않기 때문에 위의 방법에 비해 걸리는 시간이 훨씬 적다.

"""
a < b 라고 가정하고 
a부터 b까지의 합은
sigma(1~b) - sigma(1~a) + a = b(b+1) / 2 - a(a+1) / 2
= (b^2 + b - a^2 - a) / 2 + a
= (b^2 + b - a^2 + a) / 2
= (b - a + 1)(b + a) / 2
따라서 a > b 일때도 고려하면 (|a-b| + 1)(a+b) / 2
"""