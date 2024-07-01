def solution(sizes):
    x_max = 1
    y_max = 1
    for i in range(len(sizes)):
        w, h = sizes[i]   # index 덜 하기 위해 값 저장
        if w < h:   # 왼쪽 좌표가 큰 값으로 바꾸기
            sizes[i] = h, w
            x_max = max(x_max, h)
            y_max = max(y_max, w)
        else:
            x_max = max(x_max, w)
            y_max = max(y_max, h)
    answer = x_max * y_max
    return answer