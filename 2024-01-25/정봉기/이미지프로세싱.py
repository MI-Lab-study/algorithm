from collections import deque
#deque는 파이썬의 내장 모듈인 collections에 속한 클래스로, 큐(Queue)와 스택(Stack)의 특징을 모두 가지음
import sys
input = sys.stdin.readline 

d = [[1,0],[0,1],[-1,0],[0,-1]]
#픽셀배열
def checkNowPixels():
    for i in range(h):
        for j in range(w):
            print(pixels[i][j], end=" ")
        print()
#그리드의 픽셀 색상을 업데이트하기 위한 BFS
# h (높이가 먼저오기때문)에 [y][x] 
def bfs(y,x, color, change):
    queue = deque()  #큐로 픽셀을 유지 디큐 이용.
    queue.append([y,x])
    print(queue)
    pixels[y][x] = change
    visited = [[False]*w for _ in range(h)]
    #queue.append([y, x]): 시작 픽셀 좌표가 대기열에 추가됩니다.
    #pixels[y][x] = 변경: 시작 픽셀의 색상이 업데이트됩니다.
    #visited: 방문한 픽셀을 추적하는 2D 배열입니다.
    #이 함수는 큐가 빌 때까지 while 루프를 실행합니다.
    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if (0<=dr<h) and (0<=dc<w) and not visited[dr][dc] and pixels[dr][dc] == color:
                visited[dr][dc] = True
                pixels[dr][dc] = change
                queue.append([dr,dc])
"""
        r, c = queue.popleft(): 대기열의 왼쪽에서 픽셀을 제거합니다.
        그런 다음 4개 방향(상하, 좌, 우) 모두에서 인접 픽셀을 확인합니다.
        인접 픽셀이 그리드 경계 내에 있고, 방문되지 않았으며, 시작 픽셀과 동일한 색상을 갖는 경우:
        visited[dr][dc] = True: 픽셀을 방문한 것으로 표시합니다.
        pixels[dr][dc] = 변경: 픽셀의 색상을 업데이트합니다.
        [dr, dc]는 추가 탐색을 위해 대기열에 추가됩니다.
""" 
h,w = map(int,input().split())
pixels = [list(map(int,input().split())) for _ in range(h)]


q = int(input()) #연산할 개수
for tmp in range(q):

    i, j, c = map(int,input().split())
    i, j = i-1, j-1 #인덱스를 위한 처리

    bfs(i,j, pixels[i][j], c)


checkNowPixels()