import sys
from collections import defaultdict
N, K = map(int, input().split())

dicts_ri = defaultdict(int)
dicts_pi = defaultdict(list)
dicts_xi = defaultdict(int)
dicts_n = defaultdict(int)
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        dicts_ri[i] = 0
        dicts_n[i] = 0
    else:
        dicts_ri[i] = temp[0]
        for j in range(1, temp[0]+1):
            dicts_pi[i].append(temp[j])
        dicts_n[i] = 0
            
for i in range(K):
    dicts_n[1] += 1
    std_node = dicts_pi[1][dicts_xi[1]]
    dicts_xi[1] += 1
    dicts_xi[1] %= dicts_ri[1]
    
    dicts_n[std_node] += 1
    while dicts_ri[std_node] != 0:
        std = std_node
        std_node = dicts_pi[std_node][dicts_xi[std_node]]
        dicts_xi[std] += 1
        dicts_xi[std] %= dicts_ri[std]
        dicts_n[std_node] += 1

output = []
for key, value in dicts_n.items():
    output.append(str(value))

sys.stdout.write(' '.join(output))
    