def solution(want, number, discount):
    answer = 0
    # number의 원소의 합이 10이므로, 10일 연속동안 다른 값이 나오면 안된다.
    want_dict = {want[i]:number[i] for i in range(len(want))}
    
    for i in range(len(discount)-9):
        search_list = discount[i:i+10]
        count_dict = {w:0 for w in want_dict}
        for item in search_list:
            if count_dict.get(item) != None:
                count_dict[item] += 1
                if count_dict[item] > want_dict[item]:
                    break
            else:   # 하나라도 count_dict에 없는 값이 나온다면 굳이 확인할 필요 없다.
                break
        if want_dict == count_dict:
            answer += 1
    return answer