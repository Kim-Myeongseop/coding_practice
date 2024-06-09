from itertools import product

def solution(users, emoticons):
    answer = []
    discount_list = [10, 20, 30, 40]
    discount_list = product(discount_list, repeat=len(emoticons))
    for discount in discount_list:   # 조합에 따라
        plus_user = 0
        total_amount = 0
        for user in users:
            amount = 0
            for i in range(len(emoticons)):
                if user[0] <= discount[i]:
                    amount += emoticons[i] * (1 - discount[i]*0.01)
            if amount >= user[1]:
                plus_user += 1
            else:
                total_amount += amount
        answer.append([plus_user, total_amount])
    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return answer[0]