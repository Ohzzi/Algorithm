n = int(input())
line = list(map(int, input().split()))
target = 1
waiting = []
line.append(n + 1)
while True:
    if line and line[0] == target:
        line.pop(0)
        target += 1
    elif waiting and waiting[-1] == target:
        waiting.pop()
        target += 1
    elif waiting and line and waiting[-1] < line[0]:
        print("Sad")
        break
    else:
        waiting.append(line.pop(0))
    if target == n + 2:
        print("Nice")
        break
