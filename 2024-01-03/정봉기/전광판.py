#아무리봐도 딕셔너리로풀어야함 나처럼 무식하게 풀면 답은 맞아도 의미없음.

import sys

def switch(number):
    if number == 1:
        return [0,0,1,1,0,0,0]
    elif number == 2:
        return [0,1,1,1,1,1,0]
    elif number == 3:
        return [0,1,1,1,0,1,1]
    elif number == 4:
        return [1,0,1,1,0,0,1]
    elif number == 5:
        return [1,1,0,1,0,1,1]
    elif number == 6:
        return [1,1,0,1,1,1,1]
    elif number == 7:
        return [1,1,1,0,0,0,1]
    elif number == 8:
        return [1,1,1,1,1,1,1]
    elif number == 0:
        return [1,1,1,0,1,1,1]
    elif number == 9:
        return [1,1,1,1,0,1,1]

def count_switch_presses(A, B):
    A_digits = [int(digit) for digit in str(A)]
    B_digits = [int(digit) for digit in str(B)]

    total_presses = 0
    for a, b in zip(A_digits, B_digits):
        a_switches = switch(a)
        b_switches = switch(b)

        for i in range(len(a_switches)):
            if a_switches[i] != b_switches[i]:
                total_presses += 1

    return total_presses

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        result = count_switch_presses(A, B)
        print(result)
