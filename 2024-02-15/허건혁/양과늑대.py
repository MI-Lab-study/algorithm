from collections import defaultdict


def solution(info, edges):
    my_dict = defaultdict(list)
    for a, b in edges:
        my_dict[a] += [b]

    result = [(1, 0, my_dict[0])]
    answer = []
    while result:
        a, b, c = result.pop()
        if c:
            for my_next in c:
                new_c = c[::]
                new_c.remove(my_next)
                new_c += my_dict[my_next]
                if info[my_next] == 0:
                    result.append((a + 1, b, new_c))
                else:
                    if a > b + 1:
                        result.append((a, b + 1, new_c))
                    else:
                        answer.append((a, b + 1, new_c))
        else:
            answer.append((a, b, c))
    return max(answer, key=lambda x: x[0])[0]
