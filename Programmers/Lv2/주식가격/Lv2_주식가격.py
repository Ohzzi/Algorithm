from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while len(queue):
        price = queue.popleft()
        day = 0
        for i in queue:
            day += 1
            if price > i:
                break
        answer.append(day)
    return answer

def stack_solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
                # stack에서 pop하면 비교 대상에서 제외된다.
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
    return answer
""" 
해당 풀이가 가능한 이유:
stack에는 prices의 인덱스를 담아둔다. 맨 처음에 0을 담아뒀으므로 for문의 i는 1부터 시작한다.
index를 stack의 맨 뒤에서 꺼내므로 무조건 index < i 이다.
따라서 prices[index] > prices[i]면 해당 인덱스의 날짜에 비해 가격이 떨어졌으므로 answer[index]를 수정해주고,
index를 stack에서 제거해 주면 된다.
떨어지지 않았다면 굳이 스택의 다른 원소들과 비교할 필요가 없이 break를 통해 i를 다음으로 넘겨주면 된다.
왜냐면 중간에 가격이 떨어지면 stack에서 이미 pop 되어 있기 때문에 stack에 들어있는 모든 인덱스에 대해서는 prices[i]가 크거나 같기 때문이다.
모든 for문을 돌면 answer를 반환하면 완성이다.
"""