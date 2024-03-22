def solution(line):
    x_list = []
    y_list = []
    
    for i in range(len(line)):
        for l in line[:i]:
            # A, B, E = line[i][0], line[i][1], line[i][2]
            # C, D, F = l[0], l[1], l[2]
            if line[i][0]*l[1] == line[i][1]*l[0]:
                continue
            x = (line[i][1]*l[2] - line[i][2]*l[1]) / (line[i][0]*l[1] - line[i][1]*l[0])
            y = (line[i][2]*l[0] - line[i][0]*l[2]) / (line[i][0]*l[1] - line[i][1]*l[0])
            
            if x == int(x) and y == int(y):
                x_list.append(x)
                y_list.append(y)
    
    x_min = min(x_list)
    y_min = min(y_list)
    x_max = max(x_list)
    y_max = max(y_list)
    
    w = int(x_max - x_min)
    h = int(y_max - y_min)
    
    answer = [['.'   for i in range(w+1)]   for j in range(h+1)]

    for i in range(len(x_list)):
        answer[int(y_min - y_list[i] - 1)][int(x_list[i] - x_min)] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer