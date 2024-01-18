from collections import defaultdict
def solution(edges):
    answer = [0,0,0,0]
    start = []
    end = []
    start.append(edges[0][0])
    end.append(edges[0][1])
    dict = defaultdict(lambda: [0,0])
    """
    list = max(start, key=start.count)
    #이런식으로 하면안됨
    #정점찾기완료
    if list not in end:
        answer[0] = list
    """
    #시작점 끝점 모으기
    for edge in edges:
        dict[edge[0]][0] += 1 #나가는 간선
        dict[edge[1]][1] += 1 #들어오는 간선
        
    
    for num, i in dict.items():
        out = i[0]
        inn = i[1]
        if out >= 2 and inn == 0:
            answer[0] = num
    #도넛 모양 그래프 찾기 (나가는거 1개 들어오는거1개 시작점재방문)?
        #if out == 1 and inn == 1:
        #    pass
            #answer[1] += 1
    #막대그래프 (주기만하고 마지막은 받기만함 -> 받기만한 경우 찾기)
        elif out == 0 and inn >= 1:
            answer[2] += 1
    #8자 그래프 (시작점 나가는거 들어오는거 2개)
        elif out >= 2 and inn >= 2 :
            answer[3] += 1
    #도넛못구해서 연결된것 중 남은거 개수로 도출
    answer[1] = dict[answer[0]][0] - answer[2] - answer[3]
    return answer
