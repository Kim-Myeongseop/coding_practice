def solution(k, room_number):
    answer = []
    total_dict = {}   # num:new_num (방:새방)
    for num in room_number:
        num_list = [num]
        while total_dict.get(num):
            num_list.append(total_dict[num])
            num = total_dict[num]
        answer.append(num)
        for n in num_list:
            total_dict[n] = num+1
    return answer