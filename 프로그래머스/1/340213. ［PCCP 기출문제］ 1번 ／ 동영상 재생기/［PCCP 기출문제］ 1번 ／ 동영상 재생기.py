def solution(video_len, pos, op_start, op_end, commands):
    video_len = (int(video_len[:2]) * 60) + int(video_len[3:])
    now = (int(pos[:2]) * 60) + int(pos[3:])
    op_start = (int(op_start[:2]) * 60) + int(op_start[3:])
    op_end = (int(op_end[:2]) * 60) + int(op_end[3:])
    if op_start <= now < op_end:
        now = op_end
        
    for command in commands:
        if command == 'next':
            now += 10
        else:   # 'prev'
            now -= 10
        
        if now < 0:
            now = 0
        elif now > video_len:
            now = video_len
        
        if op_start <= now < op_end:
            now = op_end
    
    hour = str(now//60)
    minute = str(now%60)
    if len(str(hour)) == 1:
        hour = '0' + hour
    if len(str(minute)) == 1:
        minute = '0' + minute
    answer = hour + ':' + minute
    return answer