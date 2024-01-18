def solution(friends, gifts):
    answer = 0
    length = len(friends)
    score = [0] * len(friends)

    #0. Create Table
    give = [[0] * length for _ in range(length)] # 선물은 준 횟수
    for gift in gifts:
        gift = gift.split(" ")
        giver = friends.index(gift[0])
        getter = friends.index(gift[1])

        give[giver][getter] += 1

    #1. Calculation
    for i in range(length):
        for j in range(i + 1, length):
            give_score = give[i][j] # i가 j에게 준 선물의 개수
            get_score = give[j][i] #j가 i에게 준 선물의 개수

            #1-1. 선물을 주고 받은 경우
            if (give_score != get_score) and (give_score > 0 or get_score > 0):
                if give_score > get_score:
                    score[i] += 1

                else:
                    score[j] += 1

            #1-2. 선물 지수 계산
            else:
                giver_present_score = sum(give[i])
                getter_present_score = sum(give[j])

                for k in range(length):
                    giver_present_score -= give[k][i]
                    getter_present_score -= give[k][j]


                if giver_present_score > getter_present_score:
                    score[i] += 1

                elif giver_present_score < getter_present_score:
                    score[j] += 1




    answer = max(score)
    return answer