def solution(rows, columns, queries):
    answer = []
    matrix = [[(i)*columns+j+1   for j in range(columns)]   for i in range(rows)]
    for query in queries:
        m = 10000
        r1, c1, r2, c2 = query
        
        index_list = []
        index_list.extend([(r,c1)   for r in range(r1,r2)])
        index_list.extend([(r2,c)   for c in range(c1,c2)])
        index_list.extend([(r,c2)   for r in range(r2,r1,-1)])
        index_list.extend([(r1,c)   for c in range(c2,c1,-1)])
        
        index_len = len(index_list)
        temp = matrix[index_list[0][0]-1][index_list[0][1]-1]
        for index in range(index_len-1):
            m = min(m, matrix[index_list[index][0]-1][index_list[index][1]-1])
            matrix[index_list[index][0]-1][index_list[index][1]-1] = matrix[index_list[index+1][0]-1][index_list[index+1][1]-1]
        
        m = min(m, matrix[index_list[index_len-1][0]-1][index_list[index_len-1][1]-1])
        matrix[index_list[index_len-1][0]-1][index_list[index_len-1][1]-1] = temp
    
        answer.append(m)
    
    return answer