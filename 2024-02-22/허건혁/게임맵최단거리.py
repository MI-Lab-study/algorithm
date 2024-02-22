def solution(maps):
        
    n = len(maps)     # 행
    m = len(maps[0])  # 열
    maps = [[0] * (m+2)] + [[0] + map +[0] for map in maps] + [[0] * (m+2)]
    
    new_start = []
    start = [[1,1]]
    count = 2
    
    while start:
        for st in start:
            x,y = st
            
            #위
            if maps[x][y-1] == 1:
                maps[x][y-1] = count
                new_start += [[x,y-1]]
            #아래
            if maps[x][y+1] == 1:
                maps[x][y+1] = count
                new_start += [[x,y+1]]
            #오른쪽
            if maps[x+1][y] == 1:
                maps[x+1][y] = count
                new_start += [[x+1,y]]
            
            #왼쪽
            if maps[x-1][y] == 1:
                maps[x-1][y] = count
                new_start += [[x-1,y]]
        
        if [n,m] in new_start: return count
        start = new_start
        new_start = []
        count += 1
        
    return -1