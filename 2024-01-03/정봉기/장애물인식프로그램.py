import sys

# DFS 함수: 연결된 장애물 블록의 크기를 찾음
def find_blocks(matrix, visited, row, col, block_number):
    # 경계를 벗어나거나, 이미 방문한 곳, 또는 장애물이 없는 경우에는 0을 반환
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0 or visited[row][col]:
        return 0

    visited[row][col] = True  # 현재 위치를 방문했음을 표시
    block_size = 1  # 현재 블록의 크기를 1로 초기화

    # 상하좌우를 탐색하면서 연결된 블록을 찾음
    block_size += find_blocks(matrix, visited, row + 1, col, block_number)
    block_size += find_blocks(matrix, visited, row - 1, col, block_number)
    block_size += find_blocks(matrix, visited, row, col + 1, block_number)
    block_size += find_blocks(matrix, visited, row, col - 1, block_number)

    return block_size

# 블록 수와 각 블록 내의 장애물 수를 계산하는 함수
def count_blocks(matrix):
    n = len(matrix)
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 저장하는 2D 리스트 초기화
    blocks = []  # 각 블록의 크기를 저장할 리스트

    block_number = 0  # 블록 번호 초기화
    for i in range(n):
        for j in range(n):
            # 현재 위치가 장애물(1)이면서 아직 방문하지 않은 경우
            if matrix[i][j] == 1 and not visited[i][j]:
                block_number += 1  # 새로운 블록을 발견하면 블록 번호 증가
                block_size = find_blocks(matrix, visited, i, j, block_number)  # DFS로 블록 크기 계산
                blocks.append(block_size)  # 블록 크기를 리스트에 추가

    return block_number, sorted(blocks)  # 총 블록 수와 정렬된 블록 크기 리스트 반환

# 입력 받기
N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]

# 블록 수와 각 블록 내 장애물의 수 출력
total_blocks, block_sizes = count_blocks(matrix)

print(total_blocks)  # 총 블록 수 출력
for size in block_sizes:
    print(size)  # 각 블록 내 장애물 수 출력