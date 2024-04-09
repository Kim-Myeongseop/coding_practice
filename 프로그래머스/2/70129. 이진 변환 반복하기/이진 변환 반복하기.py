def solution(s):
    ch_cnt, zero_cnt = 0, 0
    while s != '1':
        prev_len = len(s)
        s = s.replace('0', '')
        after_len = len(s)
        zero_cnt += prev_len - after_len
        
        s = bin(after_len)[2:]
        ch_cnt += 1
    answer = [ch_cnt, zero_cnt]
    return answer