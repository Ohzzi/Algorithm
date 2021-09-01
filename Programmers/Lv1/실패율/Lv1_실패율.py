def solution(N, stages):
    # 각 스테이지별로 도달한 사람의 수를 stages 리스트에서 count 해서 저장
    stages_info = [stages.count(i + 1) for i in range(N + 1)]
    # 현재 스테이지 부터 끝까지의 값을 다 더하면 현재 스테이지에 도달한 사람 수
    # 스테이지에 머물러 있는 사람 수를 도달한 사람 수로 나누는데, 도달한 사람 수가 0이면 나누지 못하므로 (0, 0) 넣어줌
    success_rate = [(stages_info[i] / sum(stages_info[i:]), i + 1)
                    if sum(stages_info[i:]) > 0 else (0, i+1) for i in range(N)]
    # 실패율만을 기준으로 정렬
    # 람다식 안 쓸 경우 x[1], 즉 스테이지 번호가 정렬에 영향을 미쳐서 틀림
    success_rate.sort(reverse=True, key=lambda x: x[0])
    return [x[1] for x in success_rate]
