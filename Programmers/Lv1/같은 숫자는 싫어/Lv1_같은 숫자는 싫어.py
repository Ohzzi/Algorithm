def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            # 리스트를 슬라이싱 하면 리스트를 반환, 빈 리스트에 써도 빈 리스트 반환
            # 리스트에 값이 없는데 answer[-1]을 하게 되면 out of range 오류
            # 리스트와 리스트를 비교해 주어야 하므로 i를 []로 감싸서 리스트로 만들어 주어야 함
            answer.append(i)
    return answer

def other_solution(arr):
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i+1:i+2]]