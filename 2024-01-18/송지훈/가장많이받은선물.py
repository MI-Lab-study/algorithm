def solution(friends, gifts):
    from collections import defaultdict
    from itertools import combinations
    
    gift_dict = defaultdict(int)
     
    for g in gifts:
        give, take = g.split(' ')
        gift_dict[give + '_' + take] += 1
        gift_dict[give + '_index'] += 1
        gift_dict[take + '_index'] -= 1
    
    l_f = len(friends)
    complete_gift = defaultdict(int)
    
    for f1, f2 in list(combinations(friends, 2)):
        if gift_dict[f1 + '_' + f2] - gift_dict[f2 + '_' + f1] == 0:
            if gift_dict[f1 + '_index'] > gift_dict[f2 + '_index']:
                complete_gift[f1] += 1
            elif gift_dict[f1 + '_index'] < gift_dict[f2 + '_index']:
                complete_gift[f2] += 1
        else:
            if gift_dict[f1 + '_' + f2] > gift_dict[f2 + '_' + f1]:
                complete_gift[f1] += 1
            elif gift_dict[f1 + '_' + f2] < gift_dict[f2 + '_' + f1]:
                complete_gift[f2] += 1
    
    r = complete_gift.values()
    
    return 0 if not r else max(r)