import sys

input = sys.stdin.readline

T = int(input())

my_dict = {
    "0": [True, True, True, True, True, True, False],
    "1": [False, True, True, False, False, False, False],
    "2": [True, True, False, True, True, False, True],
    "3": [True, True, True, True, False, False, True],
    "4": [False, True, True, False, False, True, True],
    "5": [True, False, True, True, False, True, True],
    "6": [True, False, True, True, True, True, True],
    "7": [True, True, True, False, False, True, False],
    "8": [True, True, True, True, True, True, True],
    "9": [True, True, True, True, False, True, True],
    "-": [False, False, False, False, False, False, False],
}


def sol(a, b, my_dict):
    a = "-" * (5 - len(a)) + a
    b = "-" * (5 - len(b)) + b
    answer = 0
    for idx in range(5):
        p = my_dict[a[idx]]
        q = my_dict[b[idx]]

        for i in range(7):
            if p[i] != q[i]:
                answer += 1
    return answer


result = []
for _ in range(T):
    a, b = input().rstrip().split()
    result.append(sol(a, b, my_dict))
print("\n".join(map(str, result)))
