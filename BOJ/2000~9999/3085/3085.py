def count(candies):
    n = len(candies)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candies[i][j - 1] == candies[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
        cnt = 1
        for j in range(1, n):
            if candies[j - 1][i] == candies[j][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer

n = int(input())

candies = [list(input()) for _ in range(n)]
answer = 1

for i in range(n):
    for j in range(n): # i가 행 j가 열
        if j + 1 < n:
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
            cnt = count(candies)
            if cnt > answer:
                answer = cnt
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
        if i + 1 < n:
            candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]
            cnt = count(candies)
            if cnt > answer:
                answer = cnt
            candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]
print(answer)
