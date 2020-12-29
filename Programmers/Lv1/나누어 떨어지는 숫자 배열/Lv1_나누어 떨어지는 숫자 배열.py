def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
    # 리스트 안에서 for 문을 사용해서 한 줄로 적을 수 있다.
    # return A or B: A가 False(여기서는 빈 배열)이면 B를 return한다.