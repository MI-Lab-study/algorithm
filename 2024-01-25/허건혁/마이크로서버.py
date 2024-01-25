import sys
from bisect import bisect_right

input = sys.stdin.readline

T, result = int(input()), []
for _ in range(T):
    N = int(input())
    my_list = sorted(map(int, input().rstrip().split(" ")))
    sub_result = 0
    while my_list:
        A = my_list.pop()
        if A <= 600:
            while True:
                idx = bisect_right(my_list, 900 - A)
                if idx > 0 and my_list[idx - 1] + A <= 900:
                    A += my_list[idx - 1]
                    my_list.pop(idx - 1)
                else:
                    break
        sub_result += 1
    print(sub_result)
