from itertools import product


def solution(users, emoticons):
    emoticons = [[(i, emo) for i in [10, 20, 30, 40]] for emo in emoticons]
    result = []
    for emoticon in product(*emoticons):
        answer = [0, 0]
        for user in users:
            ratio, pivot_price, price = *user, 0
            for emo in emoticon:
                r, p = emo
                if ratio <= r:
                    price += p * (100 - r) // 100
            if pivot_price <= price:
                answer[0] += 1
            else:
                answer[1] += price
        result.append(answer)

    return max(result, key=lambda x: (x[0], x[1]))
