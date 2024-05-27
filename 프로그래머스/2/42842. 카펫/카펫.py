def solution(brown, yellow):
    answer = []
    area = brown + yellow
    width = brown//2 + 2
    height = 0
    while True and width > 0:
        width -= 1
        height += 1
        if width * height == area:
            answer.append(width)
            answer.append(height)
            break
    return answer