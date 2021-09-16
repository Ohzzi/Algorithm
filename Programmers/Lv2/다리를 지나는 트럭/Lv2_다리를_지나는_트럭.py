from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    current = 0
    while True:
        answer += 1
        current -= bridge.popleft()
        if not truck_weights:
            answer += bridge_length - 1
            break
        if current + truck_weights[0] <= weight:
            current += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    return answer
