def solution(n):
    n = bin(n)[2:]
    idx = n.rfind('01')
    if idx != -1:
        head = n[:idx] + '10'
        tail = n[idx+2:]
    else:   # idx == -1 : 존재하지 않음 -> 가장 왼쪽의 1오른쪽에 0추가 후 이후는 1을 모두 오른쪽으로 이동.
        idx = n.find('1')
        head = n[:idx] + '10'
        tail = n[idx+1:]
    
    zero_cnt = tail.count('0')
    one_cnt = tail.count('1')
    answer = head + '0' * zero_cnt + '1' * one_cnt   # 1은 있더라도 오른쪽으로 가야 가장 작은 값
    return int(answer, 2)

# 다른 풀이 1 : 테스트 4(시간 초과)
# def dec2bin(num):   # decimal to binary == bin()
#     temp = []
#     while num:
#         temp.insert(0, str(num % 2))
#         num = num//2
#     return temp   # 이진법 표현은 list형으로 return

# def bin2dec(num):   # binary to decimal == int(str(num), 2) or 0bnum
#     res = 0
#     n = len(num)
#     for i in range(n):
#         res += 2**i * int(num[n-1-i])
#     return res   # 십진법 표현은 int형으로 return
    
# def solution(n):
#     temp = 0
#     bin_str = dec2bin(n)   # 2진법 list
#     for i in range(len(bin_str)-2, -1, -1):   # 가장 오른쪽의 01이 필요하다. => 가장 오른쪽의 01 -> 10
#         if bin_str[i:i+2] == ['0','1']:   # 해당 패턴이 있으면 추가
#             temp = i
#             break
#     if temp:
#         idx = temp
#         zero_cnt, one_cnt = 0, 0
#         tail = bin_str[idx+2:]
#         for c in tail:   # '01' -> '10' 으로 바꾼 후 남은 것 작업
#             if c == '0':
#                 if one_cnt > 0:
#                     zero_cnt = len(tail) - one_cnt
#                     break
#                 zero_cnt += 1
#             else:
#                 one_cnt += 1
#         answer = bin_str[:idx] + ['1','0'] + (['0']*zero_cnt + ['1']*one_cnt)
#     else:   # 1의 왼쪽에 0이 없는 경우 가장 왼쪽 1의 오른쪽에 0을 추가
#         for i in range(len(bin_str)):
#             if bin_str[i] == '1':
#                 bin_str[i:i+1] = ['1','0']   # i 번째인 '1'을 '1','0' 으로 바꾸기
#                 answer = bin_str[:i+2] + bin_str[i+2:][::-1]
#                 break 
#     return bin2dec(answer)