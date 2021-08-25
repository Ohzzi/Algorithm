from itertools import permutations


# 입력한 숫자가 소수인지 판별할 함수
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    # 가능한 숫자 조합을 저장할 set. 중복을 제거해야 하므로 set으로 생성.
    possible_nums = set()

    for i in range(1, len(numbers) + 1):
        # 순열을 이용해 set의 합집합 연산으로 중복 배제
        possible_nums |= set([int("".join(num)) for num in [nums for nums in permutations(numbers, i)]])

    # 뽑아낸 숫자들이 소수인지 판별
    for num in possible_nums:
        if is_prime(num):
            answer += 1
    return answer
