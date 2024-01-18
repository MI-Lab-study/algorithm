# 실패한 case
def func(temp, tops, total_num):
    if not tops:
        return 1
    k = tops.pop(0)
    for pre in temp:
        if k ==1:
            if pre == 2:
                temp_new = [1,2,3]
            else:
                temp_new = [0,1,2,3]
        else:
            if pre == 2:
                temp_new = [2,3]
            else:
                temp_new = [0,2,3]
        total_num += len(temp_new) * func(temp_new, tops, total_num)
 
    return total_num

def solution(n, tops):
    answer = 0
    k = tops.pop(0)
    if k == 1:
        temp = [0,1,2,3]
    else:
        temp = [0,2,3]
    answer = func(temp, tops, answer)

    return answer
