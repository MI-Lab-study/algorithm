import sys
from collections import defaultdict, deque

# input
input = sys.stdin.readline
N, K = map(int, input().split())
graph, in_count = defaultdict(list), defaultdict(int)
for i in range(1, N + 1):
    value = list(map(int, input().split()))[1:]
    graph[i] = value
    for n in value:
        in_count[n] += 1

# 위상정렬
Q, topo = deque([1]), []
while Q:
    now = Q.popleft()
    topo.append(now)
    for next in graph[now]:
        in_count[next] -= 1
        if in_count[next] == 0:
            Q.append(next)

# result 구하기
result = defaultdict(int)
result[1] = K
for t in topo:
    nexts = graph[t]
    number, length = result[t], len(nexts)
    if length:
        q, r = number // length, number % length
        for idx, next in enumerate(nexts):
            result[next] += (q + 1) if idx < r else q

print(" ".join([str(result[i]) for i in range(1, N + 1)]))
