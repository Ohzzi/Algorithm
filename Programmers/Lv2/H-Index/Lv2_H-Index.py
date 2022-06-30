def solution(citations):
    h = []
    for i in range(max(citations) + 1):
        count = sum(1 for c in citations if c >= i)
        if count >= i:
            h.append(i)
    return max(h)
