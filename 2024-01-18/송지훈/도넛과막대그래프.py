# 시간 초과

def solution(edges):
    from collections import defaultdict

    starts = defaultdict(list)
    ends = defaultdict(int)  # 몇개 받음

    generated_point = 0

    for e in edges:
        starts[e[0]].append(e)
        ends[e[1]] += 1

    eight = []

    for key in starts.keys():
        if len(starts[key]) >= 2:
            if ends[key] == 0:
                generated_point = key
            else:
                eight.append(key)
    
    connected_point_not_eight = []   # 연결된 것 다 저장
    
    for x in starts[generated_point]:
        ends[x[-1]] -= 1
        
        if not x[-1] in eight:
            connected_point_not_eight.append(x[-1])
    
    del starts[generated_point]
    
    donut = 0
    stick = 0

    for center in eight:    # 3, 11
        for hubo in starts[center]:    # [3,5], [3,8]
            start = hubo[-1]

            while start != center:
                if start in connected_point_not_eight:
                    connected_point_not_eight.remove(start)
                    break
                start = starts[start][0][-1]


    for start in connected_point_not_eight:
        if not starts[start]:
            stick += 1
        else:
            next = starts[start][0][1]  # 처음 리스트(어차피 1개)의 다음 숫자

            while next != start:
                if not starts[next]:  # 다음 숫자에 대하여 빈 리스트이면
                    stick += 1
                    break
                else:
                    next = starts[next][0][1]  # 다음 숫자 넘겨줌
            else:
                donut += 1

    answer = [generated_point, donut, stick, len(eight)]

    return answer
