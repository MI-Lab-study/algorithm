import sys
from collections import defaultdict, deque

input = sys.stdin.readline
H, W = map(int, input().split())
xy2color = defaultdict(int)
for i in range(H):
    for j, v in enumerate(map(int, input().split())):
        xy2color[(i + 1, j + 1)] = v

Q = int(input())
for _ in range(Q):
    i, j, v = map(int, input().split())
    pivot = xy2color[(i, j)]
    if v != pivot:
        visit = defaultdict(bool)
        nexts = deque([(i, j)])
        while nexts:
            x, y = nexts.pop()
            visit[(x, y)] = True
            xy2color[(x, y)] = v
            for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + a, y + b
                if (
                    1 <= new_x <= H
                    and 1 <= new_y <= W
                    and not visit[(new_x, new_y)]
                    and xy2color[(new_x, new_y)] == pivot
                ):
                    nexts.append((new_x, new_y))

result = ""
for i in range(1, H + 1):
    result += " ".join([str(xy2color[(i, j)]) for j in range(1, W + 1)])
    result += "\n"
print(result.rstrip())
print("")
