def solution(n):
    answer = ''
    while True:
        n, r = divmod(n-1, 3)
        # 삼진법은 0, 1, 2만 있는데 문제에서는 0이 없으므로 0,1,2에 대응시켜 주기 위해 n-1
        answer = '124'[r] + answer # 0 -> 1, 1 -> 2, 2 -> 4
        if n == 0: break # n이 0 되면 종료
    return answer

def recursive_solution(n): # 재귀로 풀면 조금 더 빠름
    # 문제에서는 0이 없으므로 0,1,2에 대응시켜 주기 위해 divmod(n-1, 3)
    if n <= 3: # base case
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]
