def solution(word):
    answer = 1
    i = 4
    mul_list = [1, 6, 31, 156, 781]
    alpha_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    for char in word:
        if i == 4:
            answer += alpha_dict[char] * mul_list[i]
        if i < 4:
            answer += 1 + alpha_dict[char] * mul_list[i]
        i -= 1
        print(answer)
    return answer
    '''
    0 + i * (1 + 156*5)
    1 + i * (1 + 31*5)
    1 + i * (1 + 6*5)
    1 + i * (1 + 1*5)
    1 + i * (1 + 0*5)
    
    1자리 만들기 : 5가지
    
    2자리 만들기 : 5 x (1 + 5) = 30가지
    1 : 0,1,2,3,4,5
    2 : 0,1,2,3,4,5
    3 : 0,1,2,3,4,5
    4 : 0,1,2,3,4,5
    5 : 0,1,2,3,4,5
    
    3자리 만들기 : 5 x (1 + 30) = 155가지
    1 : 00 + 30가지
    2 : 00 + 30가지
    3 : 00 + 30가지
    4 : 00 + 30가지
    5 : 00 + 30가지
    
    4자리 만들기 : 5 x (1 + 155) = 780가지
    
    5자리 만들기 : 5 x (1 + 780) = 3905
    '''