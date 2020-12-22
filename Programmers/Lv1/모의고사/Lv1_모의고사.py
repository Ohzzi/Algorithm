def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    """
    for i in range (len(answers)):
        if first[i%5] == answers[i]:
            score[0] += 1
        if second[i%8] == answers[i]:
            score[1] += 1
        if third[i%10] == answers[i]:
            score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    """
    for i, ans in enumerate(answers):
        # range 대신 enumerate 사용. enumerate(answers)는 (index, value)를 반환
        if first[i%5] == ans:
            score[0] += 1
        if second[i%8] == ans:
            score[1] += 1
        if third[i%10] == ans:
            score[2] += 1
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    return answer
    
