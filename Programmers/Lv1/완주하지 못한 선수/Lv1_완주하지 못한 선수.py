def solution(participant, completion):
    d = dict()
    hashValue = 0
    for p in participant:
        d[hash(p)] = p
        hashValue += hash(p)
    for c in completion:
        hashValue -= hash(c)
    return d[hashValue]

# collection 사용하는 방법
"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""