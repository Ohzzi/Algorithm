def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 상하 움직임
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next = i + 1

        # name에서 A가 연속적으로 나오는 경우 오른쪽으로 계속 가는 것 보다 A가 나오기 전 지점까지만 갔다가
        # 다시 뒤로 돌아서 마지막으로 연속해서 나오는 A 앞까지 가는 경우 더 조금 움직이는 경우가 있다.
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, 2 * i + len(name) - next)

    # 좌우 움직임
    answer += min_move

    return answer
