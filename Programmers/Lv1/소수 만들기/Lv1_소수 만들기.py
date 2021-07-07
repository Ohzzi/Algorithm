from itertools import combinations

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    nums = list(combinations(nums, 3))
    for items in nums:
        num = items[0] + items[1] + items[2]
        if isPrime(num):
            answer += 1
    return answer