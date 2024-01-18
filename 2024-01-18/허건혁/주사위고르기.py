from itertools import product, combinations
from collections import Counter


def win(A, B):
    A = Counter(map(sum, product(*A)))
    B = Counter(map(sum, product(*B)))

    result = 0
    for A_key in A:
        for B_key in range(A_key):
            result += B.get(B_key, 0) * A[A_key]
    return result


def solution(dice):
    n, answer = len(dice), []
    for a in combinations(range(1, n + 1), n // 2):
        b = set(range(1, n + 1)) - set(a)

        A = [dice[i - 1] for i in a]
        B = [dice[i - 1] for i in b]

        win_count = win(A, B)
        answer.append((win_count, a))

    return max(answer)[1]
