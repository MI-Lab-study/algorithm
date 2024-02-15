def solution(board, skill):
    N, M = len(board), len(board[0])
    prefix_sum = [[0 for _ in range(M)] for _ in range(N)]

    for s in skill:
        t, r1, c1, r2, c2, d = s
        d = d if t == 2 else -d
        prefix_sum[r1][c1] += d
        if c2 + 1 < M:
            prefix_sum[r1][c2 + 1] -= d
        if r2 + 1 < N:
            prefix_sum[r2 + 1][c1] -= d
        if c2 + 1 < M and r2 + 1 < N:
            prefix_sum[r2 + 1][c2 + 1] += d

    for r in range(N):
        for c in range(M - 1):
            prefix_sum[r][c + 1] += prefix_sum[r][c]

    for c in range(M):
        for r in range(N - 1):
            prefix_sum[r + 1][c] += prefix_sum[r][c]

    result = 0
    for r in range(N):
        for c in range(M):
            if prefix_sum[r][c] > -board[r][c]:
                result += 1

    return result
