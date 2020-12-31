def solution(strings, n):
    strings = [(str[n], str) for str in strings]
    strings.sort(key=lambda x:(x[0], x[1]))
    answer = [str[1] for str in strings]
    return answer

def short_solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))