from collections import deque
def solution(queue1, queue2):
    std_len = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = (sum1+sum2)//2
    
    if sum1 == total:
        return 0
    
    std_num = 0
    std = 0
    while sum1 != total:
        if sum1 > total:
            pop_num = queue1.popleft()
            sum1 -= pop_num
            queue2.append(pop_num)
            std_num += 1
        elif sum1 < total:
            pop_num = queue2.popleft()
            sum1 += pop_num
            queue1.append(pop_num)  
            std_num += 1
        std += 1
        if std > std_len * 3:
            return -1
    return std_num