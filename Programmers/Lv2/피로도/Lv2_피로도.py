from itertools import permutations

def count_available(k, order):
    count = 0
    for dungeon in order:
        if k >= dungeon[0]:
            count += 1
            k -= dungeon[1]
    return count

def solution(k, dungeons):
    orders = permutations(dungeons, len(dungeons))
    answer = max([count_available(k, order) for order in orders])
    return answer
