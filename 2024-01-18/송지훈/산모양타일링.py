# 시간 초과

def solution(n, tops):
    from itertools import product

    total = 0

    if n == 1:
        return 4

    # 부서진 조각 때문에 만약 바로 전 step에서 1을 선택했다면 2+t를 가져오더라도 1을 빼줘야함

    choose = [0, 1]  # 0은 부서진 조각, 1은 부서지지 않은 조각 선택

    # 즉 0000000, 0000001 같은 모든 이진수 조합 생각해볼 수 있음 단, 마지막은 제외
    for x in product(choose, repeat=n-1):
        pr = 1

        for i in range(n-1):    # 마지막만 제외하고 모두 곱해줌
            ith_prod_list = [1, 2+tops[i]]  # [1, 2+t] or [2+t, 3+t]

            if i == 0:
                pr %= 10007
                pr *= ith_prod_list[int(x[0])]%10007
            else:
                if int(x[i - 1]) == 0:  # 조각이 부서짐
                    pr %= 10007
                    pr *= ith_prod_list[0]%10007 if int(x[i]) == 0 else (ith_prod_list[1]-1)%10007
                else:  # 조각이 안 부서짐
                    pr %= 10007
                    pr *= ith_prod_list[0]%10007 if int(x[i]) == 0 else (ith_prod_list[1])%10007

        ith_prod_list = [2+tops[n-1], 3+tops[n-1]]

        if int(x[n - 2]) == 0:  # 조각이 부서짐
            pr %= 10007
            pr *= ith_prod_list[0]%10007
        else:  # 조각이 안 부서짐
            pr %= 10007
            pr *= ith_prod_list[1]%10007
        
        pr %= 10007
        total += pr
        total %= 10007

    return total
