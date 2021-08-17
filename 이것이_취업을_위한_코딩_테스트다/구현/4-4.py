n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))  # 게임 지도 입력
visit = [[0] * m for _ in range(n)]  # 해당 위치를 방문했는지 확인하는 리스트
visit[x][y] = 1
cnt = 1
turn_cnt = 0  # 회전 횟수를 셀 변수

step = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 각 방향마다 가로 세로로 움직이는 수치를 저장한 리스트

while True:
    d -= 1  # 왼쪽부터 가니까 왼쪽으로 회전
    if d == -1:
        d = 3
    nx = x + step[d][0]
    ny = y + step[d][1]
    if game_map[nx][ny] == 0 and visit[nx][ny] == 0:
        cnt += 1
        x = nx
        y = ny
        visit[nx][ny] = 1
        turn_cnt = 0  # 회전 횟수 초기화
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:  # 회전 횟수가 4번이면 모든 방향 확인했으므로 뒤로 갈 수 있는지 확인
        nx = x - step[d][0]
        ny = y - step[d][1]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_cnt = 0

print(cnt)
