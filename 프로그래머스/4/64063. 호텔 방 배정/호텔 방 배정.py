def solution(k, room_number):
    answer = []
    total_dict = {}   # num:new_num (방:새방)
    for num in room_number:
        num_list = [num]   # 조회 방 전부 업데이트 하기 위해 기록
        while total_dict.get(num):   # 방이 이미 나갔으면 연결된 새방으로 넘어가기 위해
            num_list.append(total_dict[num])   # 조회한 방 목록에 추가
            num = total_dict[num]   # total_dict의 value를 이용하여 새방으로 이동
        answer.append(num)   # 방이 비었으면 while문이 끝나므로 배정
        for n in num_list:   # 배정 후 조회한 모든 방의 value를 배정된 방 다음방(+1)을 새방으로 연결
            total_dict[n] = num+1
    return answer