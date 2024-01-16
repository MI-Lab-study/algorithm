def solution(queue1, queue2):
    q = queue1 + queue2

    total_len = len(q)

    s_q1 = sum(queue1)
    total = s_q1+sum(queue2)
    half = total//2

    start, start2 = 0, total_len//2     # len(queue1)이랑 동일

    trial = 0

    if total/2 != half:
        return -1

    while start2 < total_len:
        if s_q1 > half:
            s_q1 -= q[start]
            start += 1

            trial += 1
        elif s_q1 < half:
            s_q1 += q[start2]
            start2 += 1

            trial += 1
        else:
            return trial

    return -1