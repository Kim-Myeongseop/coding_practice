from string import ascii_uppercase

def solution(name):
    alphabet_list = list(ascii_uppercase)
    n = len(name)
    answer = 0
    idx_list = []   # 'A'가 아닌 index만 저장
    for i in range(n):
        if name[i] != 'A':
            if i != 0:   # 0은 언제나 지나가야하는 대상이므로 빼고 생각한다.
                idx_list.append(i)
            idx = alphabet_list.index(name[i])
            answer += min(idx, 26-idx)   # idx_list에 저장 후엔 알파벳 최소 변경 횟수를 더해준다.
            
    max_dis = 0   # 원으로 연결했다고 했을 때, 가장 먼 간격을 구하고 그 부분을 제외하면 된다.
    left, right = 0, 1   # 무조건 index 0 에서 출발해야 하므로, 둘 중 한쪽에서 시작하기 위해 이동해야한다.
    for i in range(len(idx_list)):
        dis = abs(idx_list[i] - idx_list[i-1])
        if i == 0:
            dis = n - dis
        if dis > max_dis:
            max_dis = dis
            left, right = i-1, i
    
    if not idx_list:   # 'A'로만 이루어진 글자 처리
        return 0
    left_dis = min(idx_list[left], n - idx_list[left])
    right_dis = min(idx_list[right], n - idx_list[right])
    answer += n - max_dis
    answer += min(left_dis, right_dis)
    return answer

'''
원으로 연결한다고 했을 때, 가장 긴 간격을 빼고, 그 간격을 이루는 두 점을 양 끝으로 하여 모든 점을 지나야한다.
즉, 반드시 지나야 하는 거리는 언제나 같다. 하지만 출발점이 항상 index 0 이므로, 양 끝 점 중 더 가까운곳으로 이동하고 반대점으로 이동하는 거리가 가장 짧다.
'''