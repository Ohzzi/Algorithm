def solution(new_id):
    characters = ['-', '_', '.']
    # 1단계: 소문자로 치환
    answer = new_id.lower()
    # 2단계: 조건에 안맞는 문자 제거 
    answer_list = list(answer)
    for i in answer_list[:]:
        if not(i.islower()) and not(i.isdigit()) and not(i in characters):
            answer_list.remove(i)
    # 3단계: 마침표 중복 제거
    i = 0
    while i < len(answer_list) - 1:
        if answer_list[i] == '.' and answer_list[i+1] == '.':
            del answer_list[i+1]
        else:
            i = i + 1
    # 4단계: 마침표 처음과 끝 제거
    print(answer_list)
    if answer_list[0] == '.':
        del answer_list[0]
    if len(answer_list) > 0 and answer_list[len(answer_list) - 1] == '.':
        del answer_list[len(answer_list) - 1]
    # 5단계: 빈 문자열 채우기
    if len(answer_list) == 0:
        answer_list = ['a']
    # 6단계: 문자열 길이 조절
    if len(answer_list) > 15:
        answer_list = answer_list[:15]
        if answer_list[14] == '.':
            del answer_list[14]
    # 7단계: 길이 2자 이하일 경우
    while len(answer_list) <= 2:
        answer_list.append(answer_list[len(answer_list) - 1])
    answer = "".join(answer_list)
    return answer