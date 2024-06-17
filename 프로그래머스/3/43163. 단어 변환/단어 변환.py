from collections import deque   # stack(bfs), queue(dfs) 구현

def solution(begin, target, words):
    answer = 0
    
    # visited, linked 생성
    linked = {begin:[]}
    visited = {}
    for w in words:
        diff_cnt = 0
        for i in range(len(begin)):
            if begin[i] != w[i]:
                diff_cnt += 1
        if diff_cnt == 1:
            linked[begin].append(w)
    for word in words:
        linked[word] = []
        visited[word] = False
        for w in words:
            diff_cnt = 0
            for i in range(len(word)):
                if word[i] != w[i]:
                    diff_cnt += 1
            if diff_cnt == 1:
                linked[word].append(w)
    
    # DFS(Depth-First Search)
    search_list = deque()
    search_list.append(begin)
    cnt = 0
    while search_list:
        word = search_list.pop()
        next_words = linked[word]
        if next_words:
            for next_word in next_words:
                if visited[next_word] == False:   # 방문한 적 없으면
                    search_list.append(next_word)
                    visited[next_word] = True
        cnt += 1
        if target in search_list:
            return cnt
    
    # BFS(Breadth-First Search)
    return answer