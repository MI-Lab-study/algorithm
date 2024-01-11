def solution(queue1, queue2):
    q = queue1 + queue2
    idx1, idx2 = 0, len(queue1)
    pivot, my_sum = sum(q) // 2, sum(queue1)

    count = 0
    while pivot != my_sum:
        if idx2 == len(q):
            return -1

        if pivot < my_sum:
            my_sum -= q[idx1]
            idx1 += 1
            if idx1 == idx2:
                my_sum += q[idx2]
                idx2 += 1
                count += 1
        else:
            my_sum += q[idx2]
            idx2 += 1
        count += 1
    return count
