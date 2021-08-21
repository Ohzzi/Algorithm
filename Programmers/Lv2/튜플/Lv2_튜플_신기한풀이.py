import re
from collections import Counter


def solution(s):
    # 정규 표현식으로 골라냄 -> ['2', '2', '1', '2', '1', '3', '2', '1', '3', '4']
    # Counter로 각 원소들의 개수를 세서 딕셔너리로 반환 -> {'2': 4, '1': 3, '3': 2, '4': 1}
    # sorted를 이용해 value 값이 큰 순서대로 출력
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
