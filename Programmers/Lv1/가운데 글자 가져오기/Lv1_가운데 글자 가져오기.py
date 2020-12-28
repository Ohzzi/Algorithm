def solution(s):
    q,r = divmod(len(s)-1, 2)
    return s[q:q+r+1]

def better_solution(s):
    return s[(len(s)-1) // 2 : len(s) // 2 + 1]