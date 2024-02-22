from collections import deque

def BFS(i,j,N, queue,visited, table):
    if i<0 or i>=N or j<0 or j>=N:
        return queue,visited, table, False
    
    if not visited[i][j] and table[i][j] != 0:
        visited[i][j] = True
        queue.append([i,j])
        return queue,visited, table, True
    
    return queue,visited, table, False

def isfit(game_board, coord,N):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    for x,y in coord:
        for dx,dy in d:
            if x+dx<0 or x+dx>=N or y+dy<0 or y+dy>=N:
                continue
            if [x+dx,y+dy] in coord:
                continue
            if game_board[x+dx][y+dy] == 0:
                return False
    return True
                
def rotate(game_board, N):
    game_board_temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            game_board_temp[j][N-1-i] = game_board[i][j]
    
    return game_board_temp
        
def solution(game_board, table):
    answer = 0
    # 판 회전하기
    # 시계방향 회전
    # i,j -> j,M-1-i
    
    N = len(table)
    
    visited = [[False] *N for _ in range(N)]
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    
    total_sequence = []
    
    for t in range(4):
        for i in range(N):
            for j in range(N):
                if table[i][j] != 0 and not visited[i][j]:
                    queue = deque([[i,j]])
                    sequence = deque()
                    while queue:
                        i_, j_ = queue.popleft()
                        visited[i_][j_] = True
                        for dx, dy in d:
                            queue,visited, table, do = BFS(i_+dx, j_+dy, N, queue,visited, table)
                            if do:
                                sequence.append([i_+dx-i,j_+dy-j])
                    total_sequence.append(sequence)

        for i in range(N):
            for j in range(N):
                if game_board[i][j] == 0:
                    for queues in total_sequence:
                        coord = [[i,j]]
                        queues_t = queues.copy()
                        while queues_t:
                            dx, dy = queues_t.popleft()
                            if i+dx<0 or i+dx>=N or j+dy<0 or j+dy>=N:
                                break
                            if game_board[i+dx][j+dy] != 0:
                                break
                            else:
                                coord.append([i+dx, j+dy])

                        if queues_t:
                            continue
                        else:
                            is_fit = isfit(game_board, coord,N)

                        if is_fit:
                            if len(coord) != len(queues)+1:
                                continue
                            for x,y in coord:
                                game_board[x][y] += 1
                                answer += 1
                            total_sequence.remove(queues)
                            break
        if t != 3:
            game_board = rotate(game_board, N)
    
    return answer

