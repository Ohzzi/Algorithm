def solution(s):
    answer = []
    tuples = []
    s = s.lstrip('{').rstrip('}').split("},{")
    for c in s:
        tuples.append(c.split(','))
    tuples.sort(key=len)
    for t in tuples:
        set1 = set(answer)
        set2 = set(t)
        result = list(set2 - set1)
        answer.append(result[0])
    return [int(a) for a in answer]
