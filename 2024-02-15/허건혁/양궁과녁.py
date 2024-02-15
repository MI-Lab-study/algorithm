def solution(n, info):
    info2 = [i + 1 for i in info]
    pivot = [0] * 11

    def make_all(info=pivot, depth=0):
        if depth == 10:
            return [info] if sum(info) <= n else []
        A = info[:]
        B = info[:]
        A[depth] = info2[depth]
        return make_all(A, depth + 1) + make_all(B, depth + 1)

    def cal(A, B=info):
        result = 0
        for i in range(10):
            if A[i] > B[i]:
                result += 10 - i
            else:
                if not A[i] and not B[i]:
                    pass
                else:
                    result -= 10 - i
        return result

    def cal2(A):
        return sum([idx * value for idx, value in enumerate(A)])

    result = []
    my_max = 0
    for i in make_all():
        sco = cal(i)
        if sco > my_max:
            my_max = sco
            result = i
        elif sco == my_max:
            result = i if cal2(i) > cal2(result) else result

    if not my_max or not result:
        return [-1]  # 동점이거나 이기는 경우가 없을 때
    if sum(result) < n:
        result[-1] += n - sum(result)
    return result
