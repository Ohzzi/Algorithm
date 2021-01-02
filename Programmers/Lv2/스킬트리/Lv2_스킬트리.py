from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        index = []
        for i in skill:
            index.append(s.find(i))
        if all(x < y and x != -1 or y == -1 for x, y in zip(index[:-1], index[1:])):
            # x가 -1이면 선행 스킬을 배울 수 없으므로 무조건 정답이 아님
            # or y == -1 인 조건은 만약 y가 -1이면 x > y 인데 선행 스킬 조건에는 부합하므로 제외해주기 위함
            answer += 1
    return answer

# 대부분의 테스트에서 미세하게 빠른 속도를 보이고, 1개 테스트에서 훨씬 빠른 속도를 보여줌
# 훨씬 효율적인 풀이
def other_solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = deque(list(skill))

        # Python은 for - else 문을 지원한다. for문이 중간에 끊기지 않으면 else 문을 수행한다.
        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
            # s가 skill에 포함되어 있으면(스킬트리에 들어있으면), skill_list.popleft()인지 확인
            # skill_list.popleft()이 현재 남은 가장 선행 스킬이므로 != 이면 선행 스킬을 찍지 않음
        else:
            answer += 1

    return answer