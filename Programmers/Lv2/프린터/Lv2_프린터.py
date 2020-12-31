from collections import deque

def solution(priorities, location):
    answer = 0
    # max()로 priority의 최대값을 구하기 위해 idx와 value의 순서를 바꾼다
    queue = deque([(value, idx) for idx, value in enumerate(priorities)])
    # deque의 popleft()는 O(1), queue의 pop(0)은 O(N)이라 deque로 푸는게 더 효율적
    while len(queue):
        front = queue.popleft()
        if queue and front[0] < max(queue)[0]: # front의 priority가 queue 안에서의 최댓값보다 작으면
            queue.append(front) # queue의 맨 뒤로 front를 보낸다
        else:
            answer += 1 # 아니면 출력하므로 출력 횟수를 저장하는 answer += 1
            if front[1] == location:
                return answer
    return answer

def other_solution(priorities, location):
    # any를 사용한 풀이
    queue =  deque([(i,p) for i,p in enumerate(priorities)])
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue): # any: iteration 중에 하나라도 True 면 True 반환
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer