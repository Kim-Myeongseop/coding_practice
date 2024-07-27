import string

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        MAX_COST = float('inf')
        str2num = {string.ascii_lowercase[i]:i for i in range(26)}
        n = len(original)

        transformation = [[MAX_COST]*26 for _ in range(26)]
        for i in range(n):
            o = str2num[original[i]]
            c = str2num[changed[i]]
            transformation[o][c] = min(transformation[o][c], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if i == j:
                        transformation[i][j] = 0
                        continue
                    via = transformation[i][k] + transformation[k][j]
                    if transformation[i][j] > via:
                        transformation[i][j] = via
        
        answer = 0
        for i in range(len(source)):
            value = transformation[str2num[source[i]]][str2num[target[i]]]
            if value == MAX_COST:
                answer = -1
                break
            else:
                answer += value
        return answer
        