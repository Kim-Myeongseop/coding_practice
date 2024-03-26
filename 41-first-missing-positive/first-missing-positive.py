class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = 1
        nums.sort()
        for num in nums:
            if num == temp:
                temp += 1
        return temp