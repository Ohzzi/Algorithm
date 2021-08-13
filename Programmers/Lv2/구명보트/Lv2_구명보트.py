from collections import deque


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    while len(people) != 0:
        if len(people) == 1:
            people.pop()
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        answer += 1

    return answer


def other_solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
