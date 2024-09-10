def solution(gems):
    answer = []
    total_length = len(gems)
    unique_length = len(set(gems))
    
    gem_dict = {gems[0]:1}
    r = 0   # right pointer
    for l in range(total_length):   # left pointer
        if l > r:   # l이 r보다 오른쪽으로 가면, r이 이전 iter에 안움직였다는 의미(unique 길이 만족)
            answer = [(l-1) + 1, r + 1]   # 이후는 확인할 필요 없다.(최초로 발생한 길이 0이 무조건 정답)
            break
        
        if l > 0:   # 이전 것 제거
            if gem_dict[gems[l-1]] == 1:
                gem_dict.pop(gems[l-1])
            else:
                gem_dict[gems[l-1]] -= 1
            
        while r < total_length:
            if len(gem_dict) == unique_length:
                if not answer or (r - l) < (answer[1] - answer[0]):   # 기존 answer보다 짧으면 추가
                    answer = [l+1, r+1]
                break
            
            r += 1   # unique 길이가 될 때 까지 r을 오른쪽으로 이동
            if r == total_length:   # 이후로는 while문을 돌지 않는다. (즉, answer 업데이트가 안됨)
                return answer
            if gem_dict.get(gems[r]):
                gem_dict[gems[r]] += 1
            else:
                gem_dict[gems[r]] = 1
    return answer