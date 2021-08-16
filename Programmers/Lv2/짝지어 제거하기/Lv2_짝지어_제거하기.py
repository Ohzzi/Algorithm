def solution(s):
    stack = []
    for c in s:
        # 스택에 아무것도 없으면 스택에 추가
        if not stack:
            stack.append(c)
        # 스택의 맨 끝과 c가 같으면 연속되는 문자열이므로 스택에서 제거
        elif c == stack[-1]:
            stack.pop()
        # 이외의 경우 스택에 추가
        else:
            stack.append(c)
    return 1 if not stack else 0
