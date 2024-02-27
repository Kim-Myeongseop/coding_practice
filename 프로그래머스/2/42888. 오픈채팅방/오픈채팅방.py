def solution(record):
    answer = []
    user_dict = {}
    
    for r in record:
        r_lst = r.split()
        
        if r_lst[0] == 'Enter':
            answer.append(f'{r_lst[1]}님이 들어왔습니다.')
            if not user_dict.get(r_lst[1]):   # 첫 입장
                user_dict[r_lst[1]] = r_lst[2]
            else:
                user_dict[r_lst[1]] = r_lst[2]
            
        if r_lst[0] == 'Leave':
            answer.append(f'{r_lst[1]}님이 나갔습니다.')
            
        if r_lst[0] == 'Change':
            user_dict[r_lst[1]] = r_lst[2]
            
    for i in range(len(answer)):
        key = answer[i][:answer[i].index('님')]
        answer[i] = answer[i].replace(key, user_dict[key])
        
    return answer