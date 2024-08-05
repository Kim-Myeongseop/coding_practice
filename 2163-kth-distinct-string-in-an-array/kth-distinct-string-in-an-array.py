class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distincts = []
        remove_list = []
        for a in arr:
            if a in distincts:
                distincts.remove(a)
                remove_list.append(a)
            else:
                if a not in remove_list:   # 삭제 됐다가 다시 추가할 때, 이전에 지웠는지를 확인해야함
                    distincts.append(a)
        
        if k <= len(distincts):
            answer = distincts[k-1]
        else:
            answer = ''
        return answer
        