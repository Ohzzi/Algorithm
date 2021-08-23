from collections import deque


def solution(s):
    answer = len(s)
    s = deque(s)
    bracket = {')': '(', ']': '[', '}': '{'}
    for _ in range(len(s)):
        characters = []
        for c in s:
            if c in bracket:
                if characters and characters[-1] == bracket[c]:
                    del(characters[-1])
                else:
                    answer -= 1
                    break
            else:
                characters.append(c)
        else:
            if characters:
                answer -= 1
        s.rotate(-1)
    return answer


# 스택을 사용하는 다른 풀이
def check(string):
    stack = []
    for s in string:
        if len(stack) == 0:
            if s == ')' or s == '}' or s == ']':
                return False
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
    if stack:
        return False
    else:
        return True


def stack_solution(s):
    answer = 0
    queue = deque(s)
    i = 0
    while i != len(queue):
        if check(queue):
            answer += 1
        queue.rotate(-1)
        i += 1

    return answer
