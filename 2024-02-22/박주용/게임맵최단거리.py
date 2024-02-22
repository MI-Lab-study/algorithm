from collections import deque

def BFS(x,y, visited, queue, maps, M, N, std):
    if x<0 or x>=N or y<0 or y>=M:
        return visited, queue, maps
    
    if not visited[x][y] and maps[x][y] != 0:
        std += 1
        visited[x][y] = True
        maps[x][y] = std
        queue.append([x,y,std])
        
    return visited, queue, maps


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    
    visited[0][0] = True
    
    queue = deque([[0,0,1]])
    
    d = [[1,0],[-1,0], [0,1], [0,-1]]
    
    while queue:
        x,y,std = queue.popleft()

        for dx,dy in d:
            visited, queue, maps = BFS(x+dx, y+dy, visited, queue, maps, M, N, std)

    if visited[N-1][M-1]:
        return maps[N-1][M-1]
    else:
        return -1
        
    