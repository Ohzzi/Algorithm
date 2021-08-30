from itertools import combinations


def solution(orders, course):
    answer = []
    for course_len in course:
        possible = {}
        tmp = []
        for order in orders:
            tmp += list(combinations(sorted(order), course_len))
        for t in tmp:
            menu = ''.join(t)
            if menu in possible:
                possible[menu] += 1
            else:
                possible[menu] = 1
        answer += [k for k, v in possible.items() if max(possible.values()) == v and v > 1]
    return sorted(answer)
