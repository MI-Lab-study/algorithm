from collections import defaultdict


def solution(edges):
    my_dict = defaultdict(lambda: [0, 0])
    for a, b in edges:
        my_dict[a][0] += 1
        my_dict[b][1] += 1

    result = [0, 0, 0, 0]
    for key, value in my_dict.items():
        if value[0] >= 2 and value[1] == 0:
            result[0] = key
        elif value[0] == 0 and value[1] >= 1:
            result[2] += 1
        elif value[0] == 2 and value[1] >= 2:
            result[3] += 1
    result[1] = my_dict[result[0]][0] - sum(result[1:])
    return result
