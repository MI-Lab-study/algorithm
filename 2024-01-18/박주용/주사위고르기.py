# 실패한 case
from itertools import combinations
import random
from collections import defaultdict
def solution(dice):
    lists = [x for x in range(len(dice))]
    dice_lists = []
    for i in combinations(lists, len(lists)//2):
        dice_lists.append(i)
        
    dicts = defaultdict(int)
    for i in range(len(dice_lists)//2):
        for _ in range(1296):
            my_score = 0
            your_score = 0
            for dice_idx in dice_lists[i]:
                dicea = dice[dice_idx]
                idx = random.randrange(0,6)
                my_score += dicea[idx]

            for dice_idx in dice_lists[-i-1]:
                dicea = dice[dice_idx]
                idx = random.randrange(0,6)
                your_score += dicea[idx]
            if my_score > your_score:
                dicts[str(dice_lists[i])] += 1
            else:
                dicts[str(dice_lists[-i-1])] +=1
    print(dicts)

    
    answer = []
    
    return answer