n, m = map(int, input().split())
count = 0

# 4가지 이동 방법을 모두 사용하려면 세로는 최소 3칸 필요
# 가로는 한 칸 이동하는 이동과 두 칸 이동하는 이동이 두 개씩 있으므로 최소 1 + 2 + 4 = 7칸 필요
if n == 1:
    count = 1
elif n == 2:
    # 세로가 2칸이면 매번 이동에 2칸씩 소모
    # 이동 방식이 2가지 밖에 없으므로 4칸 이상 밟을 수 없다.
    count = min(4, (m - 1) // 2 + 1)
elif m < 7:
    # 세로가 3칸이면 매 이동 시 가로 1칸만 움직이는 경우가 가장 많이 움직일 수 있음
    # 그러나 가로가 7칸이 안 될 경우 최대 3번만 이동 가능(4칸 방문)
    count = min(4, m)
else:
    # 4가지 이동 방법을 모두 사용하는데 7칸 필요
    # 가로가 7칸이 넘어가면 4가지 이동 방법 + 위아래로 움직이는 것(가로 1칸 세로 2칸)이 가장 효율이 좋음
    # 따라서 가로 7칸 넘어간 이후는 남는 가로 칸 수 만큼 + 7칸까지 4가지 이동 방법을 사용할 때 칸 수 5
    # 5 + (m - 7) = m - 2
    count = m - 2

print(count)
