from collections import deque

def printer_queue():
    n, m = map(int, input().split())
    printer = deque([(priority, idx) for idx, priority in enumerate(map(int, input().split()))])
    answer = 0
    while True:
        doc = printer.popleft()
        if printer and doc[0] < max(printer)[0]:
            printer.append(doc)
        else:
            answer += 1
            if doc[1] == m:
                return answer

t = int(input())
for _ in range(t):
    print(printer_queue())
