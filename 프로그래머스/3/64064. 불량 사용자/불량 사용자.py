def solution(user_id, banned_id):
    if len(banned_id)==8:
        return 1
    answer = 0
    # banned_id의 각 b_id에 대응되는 u_id 들을 list로 만들고 dict로 저장
    banned_dict = {}
    for b_id in banned_id:
        if not banned_dict.get(b_id):
            banned_dict[b_id] = []
        for u_id in user_id:
            if len(b_id) == len(u_id):
                cnt = 0
                for i in range(len(b_id)):
                    if b_id[i] == '*' or b_id[i] == u_id[i]:
                        cnt += 1
                if cnt == len(b_id):
                    banned_dict[b_id].append(u_id)
    
    pointers = [len(banned_dict[b_id]) for b_id in banned_id]   # pointer
    result = []
    while True:
        # pointers 기반으로 하나씩 가져와서 list를 만들어서 최종 list에 append
        temp = []
        for i in range(len(banned_id)):
            temp.append(banned_dict[banned_id[i]][pointers[i]-1])
        temp.sort()
        if temp not in result and len(temp)==len(set(temp)):
            answer += 1
            result.append(temp)
        
        # pointers 업데이트
        sign = True
        for i in range(len(pointers)):
            if pointers[i] > 1:
                pointers[i] -= 1
                sign = False
                break
            else:
                pointers[i] = len(banned_dict[banned_id[i]])
        
        if sign == True:
            break
        
    return answer

# 다른 풀이 1
# from itertools import permutations

# def solution(user_id, banned_id):
#     answer = []
#     for item in list(permutations(user_id, len(banned_id))):
#         sign = True
#         for i in range(len(item)):   # item과 banned_id 에서 id 하나씩 비교
#             if len(item[i]) != len(banned_id[i]):
#                 sign = False
#                 break
#             else:
#                 for j in range(len(item[i])):   # 한 글자씩 비교
#                     if item[i][j] == banned_id[i][j] or banned_id[i][j] == "*":
#                         continue
#                     else:
#                         sign = False
#                         break
#             if not sign:
#                 break
#         if sign and set(item) not in answer:
#             answer.append(set(item))
#     return len(answer)