def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    answer = n - len(_lost)
    for i in _lost:
        if i-1 in _reserve:
            _reserve.remove(i-1)
            answer += 1
        elif i+1 in _reserve:
            _reserve.remove(i+1)
            answer += 1
    return answer