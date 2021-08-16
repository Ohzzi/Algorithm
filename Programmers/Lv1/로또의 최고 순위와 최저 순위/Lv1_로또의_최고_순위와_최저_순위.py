def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    lottos.sort(reverse=True)
    for lotto in lottos:
        if lotto == 0:
            break
        elif lotto in win_nums:
            cnt += 1
    answer.append(rank[cnt + lottos.count(0)])
    answer.append(rank[cnt])
    return answer
