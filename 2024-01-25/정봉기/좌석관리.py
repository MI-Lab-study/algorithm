"""
import sys
from collections import defaultdict,deque
import math
input = sys.stdin.readline

#사회적거리두기
#NxM 행렬 좌표배정 (x,y) 가로세로 안되고 가장 가까운거리
#최솟값찾기

#좌석배정

#좌석 나가!
    
# In인 경우 id 값이 있을떄, already seated
# In인 경우 id 값이 없을때, already ate lunch
# 배정x There are no more seats
# 앉을때, {id} gets the seat ({x},{y})

# out id 값이 없을 때, didn't eat lunch
# 있다 없을 때, already left seat
# 실행 완 leaves from the seat ({x},{y})



N,M,Q = map(int,input().split())
K = N*M
list = []
for i in range(N):
    for j in range(M):
        list[i][j] = 0 
queue = deque()  #큐로 유지 디큐 이용
id_dict = defaultdict(int)
queue.append([1,1])
for i in range(Q-1):
    oper,id = map(str,input().split())
    if oper == 'In'and id_dict == None:
        if id not in id_dict:
            id_dict[id] = queue[0]
            print(f'{id} gets the seat {id_dict[id]}')
        else:
            print(f'{id} already seated')

    elif oper == 'In' and id_dict != None:
        
    
        for n in range(N):
            for m in range(M):
                list[n][m] = (math.sqrt((queue[i][0]-n)^2+(queue[i][1]-m)^2))
        [n,m] = list.index(max(list))
        if [n.m] not in list:
            queue[i+1] = [n,m]
            id_dict[id] = queue[i+1]
            if id not in id_dict:
                print(f'{id} gets the seat {id_dict[id]}')
            elif id in id_dict:                   
                print(f'{id} already seated')
                
    elif oper == 'In' and queue[i] != None:
        print('There are no more seats')
        
    elif oper == 'Out' and id not in id_dict:
        print(f"{id} didn't eat lunch")
        
    elif oper == 'Out' and id in id_dict:
        print(f'{id} leaves from the seat {id_dict[id]}')
"""

import sys
from collections import defaultdict, deque
import math

input = sys.stdin.readline

N, M, Q = map(int, input().split())
K = N * M
seats = [[0] * M for _ in range(N)]
queue = deque()
id_dict = defaultdict(lambda: None)

for i in range(Q):
    oper, id = map(str, input().split())

    if oper == 'In':
        if id_dict[id]:
            print(f'{id} already seated.')
        elif queue:
            x, y = queue.popleft()
            id_dict[id] = (x, y)
            seats[x - 1][y - 1] = 1
            print(f'{id} gets the seat ({x}, {y}).')
        else:
            print('There are no more seats.')

    elif oper == 'Out':
        if not id_dict[id]:
            print(f'{id} didn\'t eat lunch.')
        else:
            x, y = id_dict[id]
            id_dict[id] = None
            seats[x - 1][y - 1] = 0
            print(f'{id} leaves from the seat ({x}, {y}).')

# This part is optional, you can print the final state of the seats if needed
for row in seats:
    print(row)