from collections import defaultdict
import math
a = defaultdict(int)
def solution(fees, records):
    answer = []
    base_time, base_fee, count_time, count_fee = fees
    
    name_list = []
    for i in range(len(records)):
        time, name, types = records[i].split()
        total_time = int(time[:2])*60 + int(time[3:])
        if types == 'IN':
            a[name] -= total_time
            a[name+'_std'] += 1
        else:
            a[name] += total_time
            a[name+'_std'] -= 1
        
        if not name in name_list:
            name_list.append(name)
    name_list = sorted(name_list)     
    for name in name_list:
        if a[name+'_std'] == 1:
            a[name] += 23*60+59
        if (a[name]-base_time) > 0: 
            answer.append(base_fee + math.ceil((a[name]-base_time)/count_time) * count_fee)
        else:
            answer.append(base_fee)
        
    return answer