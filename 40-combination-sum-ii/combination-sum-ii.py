class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(list(filter(lambda x: x<=target, candidates)))
        answer = []
        n = len(candidates)

        def backtrack(start, total, combi):
            if total == 0:
                answer.append(combi[:])
            elif total < 0:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, total-candidates[i], combi + [candidates[i]])
        backtrack(0, target, [])
        return answer