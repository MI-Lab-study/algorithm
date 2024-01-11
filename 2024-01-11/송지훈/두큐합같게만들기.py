def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    # 큐1의 합이 반드시 큼
    if sum_q2 > sum_q1:
        queue1, queue2 = queue2, queue1
        sum_q1, sum_q2 = sum_q2, sum_q1
    elif sum_q1 == sum_q2:
        return 0

    # 총합
    total = sum_q1 + sum_q2

    s = 0
    trial = 0

    # 대소 관계가 바뀌면 반대로도 해봐야함 그런데 또 대소 관계가 바뀐다? 이건 불가능한 것
    if total/2 != total//2:
        return -1
    
    while s <= total:
        r = queue1.pop(0)
        queue2 += [r]

        sum_q1 -= r
        sum_q2 += r

        if sum_q1 < sum_q2:
            queue1, queue2 = queue2, queue1
            sum_q1, sum_q2 = sum_q2, sum_q1
            trial += 1

        elif sum_q1 == sum_q2:
            trial += 1
            return trial
        else:
            trial += 1
        
        s+=1
            
    return -1