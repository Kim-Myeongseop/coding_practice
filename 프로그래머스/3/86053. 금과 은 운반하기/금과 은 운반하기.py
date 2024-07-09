def solution(a, b, g, s, w, t):
    N = len(g)
    max_time = 2e+9 * (2e+5//N)   # a,b 모두 1e+9이고, w는 모두 1 t는 모두 1e+5(편도)
    
    left = 0
    right = max_time
    while left < right:
        # 총 합의 최대 금 / 최소 은 ~ 최소 금 / 최대 은 사이의 범위 내에 a, b가 있으면 공급 가능한 경우
        gold_max = [0, 0]   # gold 최대 / silver 최소
        gold_min = [0, 0]   # gold 최소 / silver 최대
        mid = (left+right)//2   # 걸리는 시간
        for i in range(N):
            cnt = (mid//t[i]+1)//2   # (시간을 각 시간으로 나눈 몫(총 편도 횟수) + 1) // 2 => 공급 횟수
            total = cnt * w[i]
            gold, silver = g[i], s[i]
            
            # 최대 금 / 최소 은 ~ 최소 금 / 최대 은
            if gold <= total:
                gold_max[0] += gold
                gold_max[1] += min(silver, total - gold)   # 가능한 silver 중 최대
            else:
                gold_max[0] += total
                gold_max[1] += 0
            
            if silver <= total:
                gold_min[1] += silver
                gold_min[0] += min(gold, total - silver)   # 가능한 gold 중 최대
            else:
                gold_min[1] += total
                gold_min[0] += 0
                
        # 공급 가능 여부 판단(최소 금, 최소 은이 필요량 이상 & 가능 총량이 필요량의 합 이상)
        if gold_max[0] >= a and gold_min[1] >= b and a+b <= sum(gold_max):
            right = mid
            answer = right   # 무조건 가능한 경우만 있다는 가정
        else:
            left = mid + 1
    return answer