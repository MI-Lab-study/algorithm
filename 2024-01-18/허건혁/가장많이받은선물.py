from collections import defaultdict


def comput_point(i, matrix):
    return sum(matrix[i]) - sum([m[i] for m in matrix])


def solution(friends, gifts):
    N = len(friends)
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    my_dict = dict(zip(sorted(friends), range(N)))

    for gift in gifts:
        a, b = gift.split(" ")
        matrix[my_dict[a]][my_dict[b]] += 1

    result = [0 for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > matrix[j][i]:
                result[i] += 1
            elif matrix[i][j] < matrix[j][i]:
                result[j] += 1
            else:
                i_point = comput_point(i, matrix)
                j_point = comput_point(j, matrix)
                if i_point > j_point:
                    result[i] += 1
                elif i_point < j_point:
                    result[j] += 1
    return max(result)
