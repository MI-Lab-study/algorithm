from collections import defaultdict
def solution(edges):
    dicts = defaultdict(lambda:[0,0])
    answer = [0,0,0,0]
    for edge in edges:
        dicts[(edge[0])][0] += 1
        dicts[(edge[1])][1] += 1
    
    for key, value in dicts.items():
        if value[0] >=2 and value[1] == 0:
            answer[0] += key
        elif value[0] == 0 and value[1] > 0:
            answer[2] += 1
        elif value[0] ==2 and value[1] >= 2:
            answer[3] += 1
        
    answer[1] = dicts[answer[0]][0] - answer[2] - answer[3]
    return answer