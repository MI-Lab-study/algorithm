from collections import defaultdict
import sys

input = sys.stdin.readline
N, M, Q = map(int, input().split())


def is_seat(N, M, id_seat, table):
    if not id_seat:
        return (1, 1)
    result = []
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if not table[(i, j)]:
                sub_result = []
                for a, b in id_seat.values():
                    sub_result.append([(i, j), (i - a) ** 2 + (b - j) ** 2])
                result.append(min(sub_result, key=lambda x: x[1]))
    if result:
        return max(result, key=lambda x: x[1])[0]
    return False


table = defaultdict(int)
id_seat = defaultdict(list)
is_ate = defaultdict(bool)
udlr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for _ in range(Q):
    state, id = input().rstrip().split()
    if state == "In":
        # 아직 안먹음
        if not is_ate[id]:
            v = is_seat(N, M, id_seat, table)
            if v:
                id_seat[id] = v
                x, y = v
                table[(x, y)] += 1
                for a, b in udlr:
                    if 1 <= x + a and x + a <= N and 1 <= y + b and y + b <= M:
                        table[(x + a, y + b)] += 1
                is_ate[id] = 1
                print(f"{id} gets the seat ({x}, {y}).")
            else:
                print("There are no more seats.")

        # 먹고 있음
        elif is_ate[id] == 1:
            print(f"{id} already seated.")

        # 먹고 떠남
        else:
            print(f"{id} already ate lunch.")

    else:
        # 아직 안먹음
        if not is_ate[id]:
            print(f"{id} didn't eat lunch.")

        # 먹고 있음
        elif is_ate[id] == 1:
            x, y = id_seat[id]
            del id_seat[id]
            table[(x, y)] -= 1
            for a, b in udlr:
                if 1 <= x + a and x + a <= N and 1 <= y + b and y + b <= M:
                    table[(x + a, y + b)] -= 1
            is_ate[id] = 2
            print(f"{id} leaves from the seat ({x}, {y}).")

        # 먹고 떠남
        else:
            print(f"{id} already left seat.")
