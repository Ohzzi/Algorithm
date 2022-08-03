from sys import stdin

n = int(stdin.readline())
peaks = list(map(int, stdin.readline().split()))

current_peak = peaks[0]
count = 0
answer = 0
for peak in peaks[1:]:
    if peak > current_peak:
        count = 0
        current_peak = peak
    else:
        count += 1
    answer = max(answer, count)
print(answer)
