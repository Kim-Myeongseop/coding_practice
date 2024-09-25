def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = '0' + bin(number)[2:]
        idx = len(bin_num) - 1
        visit_one = False   # 1을 만났는지
        while idx >= 0:
            if bin_num[idx] == '0' and visit_one == False:
                answer.append(int(bin_num[:idx] + '1' + bin_num[idx+1:], 2))
                break
            
            if bin_num[idx] == '1':
                visit_one = True
                if idx > 0 and bin_num[idx-1] == '0':
                    answer.append(int(bin_num[:idx-1] + '10' + bin_num[idx+1:], 2))
                    break
            
            idx -= 1
    return answer

'''
오른쪽부터 시작해서 1을 만나기 전까지 0이 하나라도 있으면, 가장 오른쪽 0을 1로 바꾸면 비트는 1개만 바뀌고,
가장 작은 수가 된다. 그런데 첫 1을 만나기 전까지 0이 없다면, 오른쪽부터 첫 01을 찾아 바꿔주면 된다.
이때, 1111 같이 0이 없는 경우를 위해 이진법으로 바꾼 후, 맨 앞에 0을 붙여준다.
101011 -> 101101
10101 -> 10110
10111 -> 11011
1111 -> 10111
'''