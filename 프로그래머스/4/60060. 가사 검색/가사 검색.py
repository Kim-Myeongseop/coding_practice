class TrieNode:
    def __init__(self, value):
        self.value = value   # 쓰지 않음
        self.isEnd = False   # 쓰지 않음
        self.children = {}   # 자식 노드의 대응 알파벳 : 자식 노드
        self.count = {}   # 깊이 : 개수(내 이후로 길이가 n인 단어의 개수)

class Trie:
    def __init__(self):
        self.root = TrieNode(value="start")
    
    def insert(self, word):
        n = len(word)
        node = self.root
        for depth, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node.count[n-depth] = node.count.get(n-depth, 0) + 1
            node = node.children[c]
        node.count[0] = node.count.get(0, 0) + 1   # 단어의 마지막 글자도 count
    
    def search_count(self, word):   # 물음표를 항상 뒤에 오게 하는 것이 계산에 유리하다.
        n = len(word)
        cnt = 0
        node = self.root
        for depth, c in enumerate(word):   # 앞은 물음표가 없음(prefix, suffix)
            if c == '?':   # ?를 만나면 현재 노드 포함, 남은 길이의 자식들의 총 개수
                cnt = node.count.get(n-depth, 0)
                break
            elif c in node.children:   # 단어에 ?가 없을 수는 없으므로,
                node = node.children[c]   # 마지막 노드의 cnt를 구할 필요는 없다.
            else:
                break
        return cnt

def solution(words, queries):
    prefix = Trie()   # 정방향 단어가 들어있는 트라이(고정 단어가 앞에 있을 때의 검색 대상)
    suffix = Trie()   # 역방향 단어가 들어있는 트라이(고정 단어가 뒤에 있을 때의 검색 대상)
    for word in words:   # 각 단어에 대해서 prefix에는 그대로, suffix에는 반대로 넣는다.
        prefix.insert(word)   # ??가 뒤에 있으면 고정 단어가 앞에 있으므로 prefix에서 검색
        suffix.insert(word[::-1])   # ??가 앞에 있으면 고정 단어가 뒤에 있으므로 뒤집어서 suffix에서 검색
        
    answer = []
    memoization = {}
    for query in queries:
        if memoization.get(query):
            answer.append(memoization[query])
            continue
        if query[0] != '?':   # ?가 뒤에 있다면, prefix에서 검색
            cnt = prefix.search_count(query)
        else:   # ?가 앞에 있다면, 뒤집어서 suffix에서 검색
            cnt = suffix.search_count(query[::-1])
        memoization[query] = cnt
        answer.append(cnt)
    return answer

# 다른 풀이 1 : Binary Search
# from bisect import bisect_left, bisect_right

# def search(word_list, start, end):   # 해당 길이 단어 리스트, 시작 글자, 종료 글자
#     left_index = bisect_left(word_list, start)   # 좌측 검색은 시작 인덱스(즉, 없으면 n)
#     right_index = bisect_right(word_list, end)   # 우측 검색은 하나 오른쪽 인덱스(즉, 없으면 0)
#     return right_index - left_index   # cnt 해당이 없으면 0이 나온다.

# def solution(words, queries):
#     answer = []
#     prefix = {}   # 단어 길이 : 정방향 단어 list
#     suffix = {}   # 단어 길이 : 역방향 단어 list
    
#     for word in words:
#         n = len(word)
#         if n not in prefix:
#             prefix[n] = [word]
#             suffix[n] = [word[::-1]]
#         else:
#             prefix[n].append(word)
#             suffix[n].append(word[::-1])
    
#     for key in prefix:   # 양 끝 단어를 찾는 방식이므로, 정렬이 필요하다.
#         prefix[key].sort()
#         suffix[key].sort()
            
#     for query in queries:
#         n = len(query)
#         if not prefix.get(n):
#             cnt = 0
#         elif query[0] != "?":   # 이번에도 역시 ?가 뒤로 가게해서 검색한다.
#             cnt = search(prefix[n], query.replace("?", "a"), query.replace("?", "z"))
#         else:   # ?가 뒤에 있으므로, ?를 모두 a로 바꾼것부터, ?를 모두 z로 바꾼것까지 포함할 수 있다.
#             cnt = search(suffix[n], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
#         answer.append(cnt)
#     return answer