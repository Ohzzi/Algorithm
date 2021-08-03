# input().split(): 공백을 기준으로 입력받음
# input().split()으로 입력받으면 iterable 한 문자들이 나오므로 int 형으로 바꿔주기 위해 map 함수 사용
n, m, k = map(int, input().split())  # n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 연속해서 더해질 수 있는 최대 횟수
data = list(map(int, input().split()))

data.sort()  # 큰 수를 더하기 위해 입력받은 수 들을 정렬

first = data[-1]
second = data[-2]

pattern = first * k + second
result = pattern * (m // (k+1)) + first * (m % (k+1))

# 책에서 나온 방법
# count = int(m / (k+1)) * k  # 반복되는 수열의 길이 k+1
# count += m % (k+1)  # 반복되는 수열 이후 m 까지 남은 횟수 만큼 가장 큰 수를 더 더해주어야 함
# result = 0
# result += first * count
# result += second * (m - count)

print(result)
