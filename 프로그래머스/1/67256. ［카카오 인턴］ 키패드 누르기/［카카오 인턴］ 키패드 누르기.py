def solution(numbers, hand):
    answer = ''
    keypad = {str(num):((num-1)//3, (num-1)%3)for num in range(1, 10)}   # 버튼 : (행, 열)
    keypad['*'], keypad['0'], keypad['#'] = (3,0), (3,1), (3,2)
    left_buttons = [key for key in keypad if keypad[key][1] == 0]
    right_buttons = ['3', '6', '9', '#']
    
    left, right = (3,0), (3,2)   # 시작 좌표
    for number in numbers:
        if str(number) in left_buttons:
            left = keypad[str(number)]
            answer += 'L'
        elif str(number) in right_buttons:
            right = keypad[str(number)]
            answer += 'R'
        else:
            row, col = keypad[str(number)]
            left_distance = abs(left[0] - row) + abs(left[1] - col)
            right_distance = abs(right[0] - row) + abs(right[1] - col)
            if left_distance < right_distance:
                left = keypad[str(number)]
                answer += 'L'
            elif left_distance > right_distance:
                right = keypad[str(number)]
                answer += 'R'
            else:   # 거리가 같다면
                if hand == 'left':   # 왼손 잡이
                    left = keypad[str(number)]
                    answer += 'L'
                else:   # 오른손 잡이
                    right = keypad[str(number)]
                    answer += 'R'
    return answer