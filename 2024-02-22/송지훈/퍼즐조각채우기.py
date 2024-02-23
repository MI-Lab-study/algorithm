def find_block(maps, visited, height, width):
    routes = []
    move = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    for i in range(height):                 # using dfs
        for j in range(width):
            if maps[i][j] == visited[0]:    # 방문하지 않았다면
                stack = []
                stack.append((i,j))
                route = [(i,j)]

                while stack:
                    x = stack[-1]
                    maps[x[0]][x[1]] = visited[1]  # 방문처리
                    moving = 0

                    for m in move:
                        new_h, new_w = x[0]+m[0], x[1]+m[1]

                        if 0 <= new_h <= height-1 and 0 <= new_w <= width-1:  # 영역 안에 들어왔다면
                            if maps[new_h][new_w] == visited[0]:     # 방문하지 않았다면
                                stack.append((new_h, new_w))
                                route.append((new_h, new_w))
                                moving = 1
                                break
                    else:
                        if moving == 0:     # 어떤 방향으로도 움직이지 못했다면 그 전으로 돌아간다
                            stack.pop()

                routes.append(route)
    return routes

def matrix_multiplication(matrix, coordinate):
    x = matrix[0][0]*coordinate[0] + matrix[0][1]*coordinate[1]
    y = matrix[1][0]*coordinate[0] + matrix[1][1]*coordinate[1]

    return (x,y)

def rotate_puzzle(puzzle, trial):       # 하나의 puzzle에 대해서만 trial번 회전
    rotate_matrix = [[0, 1], [-1, 0]]    # 회전 대응
    for _ in range(trial):            # 회전 trial번
        for idx, path in enumerate(puzzle):
            puzzle[idx] = matrix_multiplication(rotate_matrix, path)

    return puzzle

def puzzle_to_matrix(puzzle):
    x, y = zip(*puzzle)     # x는 puzzle의 모든 h들을 tuple로 y는 puzzle의 모든 w들을 tuple로
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in puzzle:
        i, j = i - min(x), j - min(y)
        table[i][j] = 1

    return table

def fill_puzzle(empty_blocks, puzzles):
    answer = 0

    for empty in empty_blocks:             # board에 있는 비어있는 공간 하나 가져옴
        filled = False
        table = puzzle_to_matrix(empty)    # board의 빈 공간을 행렬로 만듦

        for puzzle_origin in puzzles:      # puzzle들 중 하나 선택
            if filled == True:
                break

            count = len(puzzle_origin)

            for i in range(4):
                puzzle = rotate_puzzle(puzzle_origin,i)
                puzzle = puzzle_to_matrix(puzzle)

                if table == puzzle:
                    answer += count
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break
    
    return answer


def solution(game_board, table):
    height = len(table)
    width = len(table[0])
    
    empty_blocks = find_block(game_board, (0,1), height, width)     # board에서 빈 공간 퍼즐 저장    
    puzzles = find_block(table, (1,0), height, width)   # 모든 퍼즐 저장
    
    return fill_puzzle(empty_blocks, puzzles)