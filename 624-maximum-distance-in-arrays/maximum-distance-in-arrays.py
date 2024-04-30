class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_list = []
        min_list = []
        for i, array in enumerate(arrays):
            max_list.append((i, array[-1]))
            min_list.append((i, array[0]))
        max_list.sort(key=lambda x: x[1])
        min_list.sort(key=lambda x: x[1], reverse=True)
        if max_list[-1][0] == min_list[-1][0]:
            res = max(max_list[-2][1] - min_list[-1][1], max_list[-1][1] - min_list[-2][1])
        else:
            res = max_list[-1][1] - min_list[-1][1]
        return res
