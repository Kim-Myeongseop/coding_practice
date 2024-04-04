def solution(places):
    answer = []
    for place in places:
        sign = 1
        for i in range(5):
            if sign == 0:
                break
            for j in range(5):
                if sign == 0:
                    break
                if place[i][j] == 'P':
                    if i<4 and place[i+1][j] == 'P':
                        sign = 0
                        break
                    if i<3 and place[i+2][j] == 'P' and place[i+1][j] == 'O':
                        sign = 0
                        break
                    if j<4 and place[i][j+1] == 'P':
                        sign = 0
                        break
                    if j<3 and place[i][j+2] == 'P' and place[i][j+1] == 'O':
                        sign = 0
                        break
                    if i<4 and j<4 and place[i+1][j+1] == 'P' and (place[i+1][j] == 'O' or place[i][j+1] == 'O'):
                        sign = 0
                        break
                    if i>0 and j<4 and place[i-1][j+1] == 'P' and (place[i-1][j] == 'O' or place [i][j+1] == 'O'):
                        sign=0
                        break
        answer.append(sign)
    return answer