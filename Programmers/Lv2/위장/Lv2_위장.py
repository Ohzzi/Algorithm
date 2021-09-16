from collections import defaultdict


def solution(clothes):
    answer = 1
    closet = defaultdict(int)
    for c in clothes:
        closet[c[1]] += 1
    for v in closet.values():
        answer *= (v + 1)
    return answer - 1
# 해시 문제라고 분류해놓고 순열조합 지식으로 수학적으로 풀게 만드는 문제;;
