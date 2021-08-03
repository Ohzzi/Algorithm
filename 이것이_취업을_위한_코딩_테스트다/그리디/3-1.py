coin = [500, 100, 50, 10]  # 동전의 종류
n = int(input("점원이 받은 금액: "))
result = 0  # 총 사용한 동전의 개수

for c in coin:
    result += n // c
    n %= c

print(result)
