def solution(seq, n):
    last_pushed = 0
    stack = []
    answer = []
    while seq:
        if last_pushed > n:
            return ['NO']
        if not stack:
            if last_pushed > seq[0]:
                return ['NO']
            last_pushed += 1
            stack.append(last_pushed)
            answer.append('+')
        if stack[-1] < seq[0]:
            last_pushed += 1
            stack.append(last_pushed)
            answer.append('+')
        else:
            top = stack.pop()
            answer.append('-')
            if top == seq[0]:
                del(seq[0])
    return answer


n = int(input())

seq = [int(input()) for _ in range(n)]
answer = solution(seq, n)
for op in answer:
    print(op)
