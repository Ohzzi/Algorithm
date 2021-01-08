def solution(number, k):
    stack = []
    for num in number:
        while len(stack) and stack[-1] < num and k > 0:
            """
            조건 설명
            len(stack): stack에 element가 들어 있을 경우 계속 비교한다.
            stack[-1] < num: stack[-1] >= num이면 더 비교할 필요 없이 그대로 스택에 넣어도 된다.
            (어차피 stack에 들어있는 element들은 무조건 내림차순)
            k > 0: k가 0이 되면 뺄 만큼 뺐으므로 루프를 종료해도 된다.

            while 루프가 돌지 않으면 그대로 stack에 남은 num들이 저장된다.
            """
            stack.pop()
            k -= 1        
        stack.append(num) # stack에 num을 넣는다.
    return ''.join(stack[:len(stack)-k])
    """
    stack[:len(stack) - k]를 join하는 이유
    만약 for를 다 돌았는데 k가 남아있다면, 숫자가 내림차순으로 정렬되어 있는 상태
    이 때 k만큼 더 빼아하므로 뒤에서부터 제거해준다.
    """ 