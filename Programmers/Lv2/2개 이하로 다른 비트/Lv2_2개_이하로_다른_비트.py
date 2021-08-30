def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수면 가장 하위 비트가 0이므로 +1만 해주면 하위 비트 한 개만 바꾸고 가장 작은 수 만들 수 있다.
        # 따라서 +1 해 준 뒤 리스트에 추가
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            # bin으로 정수를 이진수 문자열로 바꾸면 앞에 0b 가 붙게 된다. 따라서 0b를 제거하기 위해 [2:]
            # 가장 마지막에 나온 0 다음 비트를 1로 바꿔줘야 하므로 왼쪽에 0을 추가로 붙여준다.
            bin_number = list('0' + bin(number)[2:])
            idx = ''.join(bin_number).rfind('0')
            bin_number[idx] = '1'
            bin_number[idx + 1] = '0'
            answer.append(int(''.join(bin_number), 2))
    return answer
