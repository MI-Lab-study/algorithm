import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())

my_dict = defaultdict(list)
for _ in range(N):
    a = input().rstrip()
    my_dict[a] += []

for _ in range(M):
    a, b, c = input().rstrip().split()
    my_dict[a] += [[b, c]]

result = []
for name in sorted(my_dict.keys()):
    result.append(f"Room {name}:")
    my_time = [True for _ in range(9)]

    for a, b in my_dict[name]:
        for idx in range(int(a) - 9, int(b) - 9):
            my_time[idx] = False

    sub_result = []
    my_time = [False] + my_time + [False]
    for idx, value in enumerate(my_time[:-1]):
        if value + my_time[idx + 1] == 1:
            sub_result.append(idx + 9)

    if sub_result:
        result.append(f"{len(sub_result)//2} available:")
        for i in range(len(sub_result) // 2):
            result.append(
                f"{str(sub_result[2*i]).zfill(2)}-{str(sub_result[2*i+1]).zfill(2)}"
            )
    else:
        result.append("Not available")
    result.append("-----")

print("\n".join(result[:-1]))
