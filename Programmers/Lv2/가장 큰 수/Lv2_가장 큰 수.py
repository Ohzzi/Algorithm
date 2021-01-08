import functools

def solution(numbers):
    numbers = sorted(list(map(str,numbers)), key = lambda x: x*3, reverse=True)
    if all(num == "0" for num in numbers): return "0"
    return ''.join(numbers)

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def other_solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

"""
functools 라이브러리의 cmp_to_key() 함수
비교하는 함수를 key로 변경
sorted()는 key를 인자로 받으므로 comparator(a,b)를 key로 바꿔서 전달해줌
"""