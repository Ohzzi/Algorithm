# 두 지점 간의 거리를 구하는 함수
def getDistance(location1, location2):
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])

# 숫자를 위치 좌표(튜플)로 나타내는 함수
def getPosition(number):
    number = number - 1
    return (number // 3, number % 3)

def solution(numbers, hand):
    answer = ''
    leftHand = 10 # 키패드의 *은 10이라고 생각한다
    rightHand = 12 # 키패드의 #은 12라고 생각한다
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    
    for n in numbers:
        # 키패드의 0은 11이라고 생각한다
        if n == 0:
            n = 11
        
        if n in left:
            leftHand = n
            answer = answer + 'L'
        elif n in right:
            rightHand = n
            answer = answer + 'R'
        else:
            leftDistance = getDistance(getPosition(leftHand), getPosition(n))
            rightDistance = getDistance(getPosition(rightHand), getPosition(n))
            if leftDistance < rightDistance:
                leftHand = n
                answer = answer + 'L'
            elif leftDistance > rightDistance:
                rightHand = n
                answer = answer + 'R'
            else: # leftDistance와 rightDistance가 같을 때 처리
                if hand == "left":
                    leftHand = n
                    answer = answer + 'L'
                else:
                    rightHand = n
                    answer = answer + 'R'
    
    return answer