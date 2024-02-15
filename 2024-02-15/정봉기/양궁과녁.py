from itertools import combinations_with_replacement
def compare(a,b):
    apeche = 0
    lion = 0
    for i in range(11):
        if a[i] == 0 and b[i] == 0:
            continue
        elif a[i] >= b[i]:
            apeche += 10 - i
        else:
            lion += 10 - i
    return apeche,lion

def solution(n, info):
    score_diff = 0
    possible = []
    combination = combinations_with_replacement(range(11),n)
    for comb in combination:
        lion = [0]*11
        for c in comb:
            lion[c] += 1
        apeche_score,lion_score = compare(info,lion)
        if lion_score - apeche_score > score_diff:
            possible = []
            possible.append(lion)
            score_diff = lion_score - apeche_score
        elif lion_score - apeche_score == score_diff and score_diff != 0:
            possible.append(lion)
            
    if len(possible) == 0:
        return [-1]
    
    for i in range(len(possible)):
        possible[i].reverse()
    possible.sort(reverse = True)
    possible[0].reverse()
    return possible[0]
