def solution(str1, str2):
    answer = 0
    intersection = []
    union = []

    str1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if not str1 and not str2:
        return 65536

    for s in str1:
        union.append(s)
        if s in str2:
            intersection.append(s)
            str2.remove(s)
    union += str2
    answer = int(len(intersection) / len(union) * 65536)

    return answer
