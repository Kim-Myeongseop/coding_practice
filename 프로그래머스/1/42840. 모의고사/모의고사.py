def solution(answers):
    answer = [1,2,3]
    
    p1 = [1,2,3,4,5]   # 5
    p2 = [2,1,2,3,2,4,2,5]   # 8
    p3 = [3,3,1,1,2,2,4,4,5,5]   # 10
    
    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        if p1[i%5] == answer:
            score[0] += 1
        if p2[i%8] == answer:
            score[1] += 1
        if p3[i%10] == answer:
            score[2] += 1
            
    answer = [i+1   for i in range(3)   if score[i]==max(score)]
    
    return answer