def solution(board, skill):
    answer = 0
    
    for skill_info in skill:
        types = skill_info[0]
        r1 = skill_info[1]
        r2 = skill_info[3]
        
        c1 = skill_info[2]
        c2 = skill_info[4]
        
        for i in range(r2-r1+1):
            for j in range(c2-c1+1):
                if types == 1:
                    board[i+r1][j+c1] -= skill_info[5]
                else:
                    board[i+r1][j+c1] += skill_info[5]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer +=1
    return answer