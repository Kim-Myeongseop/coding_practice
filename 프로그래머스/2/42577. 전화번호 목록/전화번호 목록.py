def solution(phone_book):   # 102.42ms
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
            answer = False
            break
    return answer

# 다른 풀이 1 : 449.39ms
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer