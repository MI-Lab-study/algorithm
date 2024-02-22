from copy import deepcopy


def solution(game_board, table):
    def rotate(A):
        R, C = len(A), len(A[0])
        new_A = [[None for _ in range(R)] for _ in range(C)]
        for r, a in enumerate(A):
            for c, value in enumerate(a):
                new_A[c][-1 - r] = value
        return new_A

    def minmax(A):
        X, Y = [], []
        for a in A:
            x, y = a
            X.append(x)
            Y.append(y)
        X.sort()
        Y.sort()
        return X[0], X[-1], Y[0], Y[-1]

    def serch(matrix, value):
        visit = deepcopy(matrix)
        R, C = len(visit), len(visit[0])
        result = []
        for r, t in enumerate(visit):
            for c, v in enumerate(t):
                if v == value:
                    my_next, answer = [(r, c)], []
                    while my_next:
                        a, b = my_next.pop()
                        visit[a][b] = 0 if value == 1 else 1
                        answer.append((a, b))
                        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            new_r, new_c = a + dr, b + dc
                            if 0 <= new_r and new_r < R and 0 <= new_c and new_c < C and visit[new_r][new_c] == value:
                                my_next.append((new_r, new_c))
                    result += [answer]

        my_result = []
        for res in result:
            u, d, l, r = minmax(res)
            sub_visit = deepcopy(visit)
            for row, col in res:
                sub_visit[row][col] = 1 if value == 1 else 0
            my_result.append([v[l : r + 1] for v in sub_visit[u : d + 1]])
        return my_result

    def compute(G, T):
        Gmax, Gmin = max(len(G), len(G[0])), min(len(G), len(G[0]))
        Tmax, Tmin = max(len(T), len(T[0])), min(len(T), len(T[0]))
        if Gmax == Tmax and Gmin == Tmin:
            for _ in range(4):
                a, b = len(G), len(G[0])
                c, d = len(T), len(T[0])
                if a == c and b == d:
                    for g, t in zip(sum(G, []), sum(T, [])):
                        if g == t:
                            break
                    if g != t:
                        return sum(sum(T, []))
                T = rotate(T)
        return False

    G_result = serch(game_board, 0)
    T_result = serch(table, 1)
    my_answer = 0
    for G in G_result:
        for idx, T in enumerate(T_result):
            v = compute(G, T)
            if v:
                my_answer += v
                T_result = T_result[:idx] + T_result[idx + 1 :]
                break

    return my_answer
