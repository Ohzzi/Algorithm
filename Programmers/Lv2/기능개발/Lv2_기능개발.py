import math

def solution(progresses, speeds):
    answer = [1]
    progresses = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]
    front = progresses.pop(0)
    for p in progresses:
        if front < p:
            answer.append(1)
            front = p
        else:
            answer[-1] += 1
    return answer

def other_solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-p) // s) for p, s in zip(progresses, speeds)]
    front = 0
    for idx, p in enumerate(progresses):
        if progresses[front] < p:
            answer.append(idx - front)
            front = idx
    answer.append(len(progresses) - front)
    return answer

def best_solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]