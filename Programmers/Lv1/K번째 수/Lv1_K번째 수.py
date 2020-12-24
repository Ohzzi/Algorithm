def solution(array, commands):
    answer = []
    for l in commands:
        answer.append(sorted(array[l[0]-1:l[1]])[l[2]-1])
        # 새 array를 만들어서 sort 하는 것 보다 sorted로 정렬된 리스트를 반환하는 것이 낫다.
    return answer

# 참고: lambda식 사용
""" 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""