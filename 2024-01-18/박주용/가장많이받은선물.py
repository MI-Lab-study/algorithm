from collections import defaultdict
def solution(friends, gifts):
    # 선물지수 = 총준선물 - 받은 선물
    # 가장 많은 선물
    # 주고 받음
    dicts = defaultdict(int)
    for gift_name in gifts:
        names = gift_name.split()
        dicts[names[0]+'_'+names[1]] += 1
        dicts[names[0]] += 1
        dicts[names[1]] -= 1
    
    dicts_total = defaultdict(int)
    for i in range(len(friends)):
        std_name = friends[i]
        for j in range(i+1, len(friends)):
            compare_name = friends[j]
            if std_name == compare_name:
                continue
            if dicts[std_name+'_'+compare_name] > dicts[compare_name+'_'+std_name]:
                dicts_total[std_name] +=1
            elif dicts[std_name+'_'+compare_name] < dicts[compare_name+'_'+std_name]:
                dicts_total[compare_name] +=1
            else:
                if dicts[std_name] > dicts[compare_name]:
                    dicts_total[std_name] +=1
                elif dicts[std_name] < dicts[compare_name]:
                    dicts_total[compare_name] +=1
    answer = 0
    for key, value in dicts_total.items():
        if answer < value:
            answer = value
        
        
    return answer