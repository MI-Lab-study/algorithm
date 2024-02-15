from itertools import combinations

def solution(n, info):
    answer = []
    
    std_num = 0
    std_n = n
    index_list = []
    peach_score = 0
    
    # 뺏어올 개수, index 찾기, 안 뺏겼을 경우의 default peach_score 구하기
    for i in range(len(info)):
        if info[i] != 0:
            std_num += 1
            std_n -= info[i]
            index_list.append(i)
            peach_score += 10-i
        if std_n == 0:
            break
    
    max_score = -9999
    # i개 훔치기
    for i in range(std_num+1):
        combi = combinations(index_list, i) # 뺏어올 index 고르는 조합
        steal_index = list(combi)
        
        for steal_tuple in steal_index:
            std_n = n
            result_list = [0] * 11 # lion 화살 결과
            result_lion = 0 # 뺏기전 peach score
            result_peach = peach_score # 뺏기기전 peach score
            how_many = 0 # 쏜 화살 수
            
            for index in steal_tuple: 
                # 뺏을 과녁점수의 peach가 쏜 화살 수 기준으로 화살 한발만 더 쏘면 뺏어오니까
                # 몇발 쐈는지 how_many에 기록
                how_many += info[index] + 1
                result_list[index] += info[index] + 1 # lion 화살 결과 기록
                
                result_lion += 10-index # 점수 뺏어오기
                result_peach -= 10-index # 점수 뺏기기
                std_n -= info[index] + 1 # 라이언 남은 화살 수
            
            # 뺏어올 수 있는 경우에서, 만약 쏠 수 있는 화살을 넘어서 쐈다면
            # 그 경우는 불가능
            if how_many > n:
                continue
            
            # 이제 나머지 경우에 쏠 수 있는 화살 할당하기 위해서
            # 어피치가 쏜 점수를 제외한 나머지에 쏠 수 있는 화살 할당하기
            t = sorted(list(set([x for x in range(11)]) - set(index_list)))
            
            
            for j in range(len(t)):
                # 쏠 수 있는 화살이 남아잇으면
                if std_n > 0:
                    std_n -= 1 # 화살 할당
                    result_lion += 10-t[j] # 라이언 점수 획득
                    result_list[t[j]] += 1 # 쏜 화살 개수 기록
            
            # 다 할당 했는데도, 남은 화살이 있으면
            # 1. 어피치가 쏜 곳 제외한 점수 중, 가장 낮은 점수에 할당하기
            # 2. 어피치가 쏜 곳 중, '위에서 뺏어오기로 한 점수에 영향을 안 주는 경우'에만 할당하기
            
            # 뺏어오기로 한 점수에 영향을 주는 경우는 
            # 현재 라이온이 특정 k 점수에 대해서, 어피치보다 쏜 개수가 낮은데, 남은 화살을 k 점수에 더 쐈을 때, 어피치의 점수를 뺏어와버리는 경우
            # 그경우 continue
            
            if std_n > 0:
                temp_list = index_list + [t[j]]
                for ind in temp_list:
                    temp_lion = result_list.copy()
                    if temp_lion[ind] < info[ind] and temp_lion[ind] + std_n > info[ind]:
                        continue
                    temp_lion[ind] += std_n
                    
                    # 최종적으로, lion이 peach보다 점수가 높으면서, max_score보다 크면
                    # max_score 변경, answer도 변경
                    if result_lion > result_peach and result_lion- result_peach > max_score:
                        max_score = result_lion - result_peach
                        answer = temp_lion
                    
                    # 만약 max_score 가 같은 경우에는
                    # 맨뒤 인덱스부터 확인하기
                    # answer가 높은 경우 있으면 break
                    # temp_lion이 높은 경우가 있으면 answer 대체하기
                    elif result_lion - result_peach == max_score:
                        for k in range(10, -1, -1):
                            if answer[k] > temp_lion[k]:
                                break
                            if temp_lion[k] > answer[k]:
                                answer = temp_lion
                                break
            
            # 할당할 화살이 없으면, result_list가 최종
            # 위 방식 동일하게 수행
            else:
                if result_lion > result_peach and result_lion- result_peach > max_score:
                    max_score = result_lion - result_peach
                    answer = result_list

                elif result_lion - result_peach == max_score:
                    for k in range(10, -1, -1):
                        if answer[k] > result_list[k]:
                            break
                        if result_list[k] > answer[k]:
                            answer = result_list
                            break
    
    if answer:
        return answer
    else:
        return [-1]