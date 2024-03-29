class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count_dict = {nums[0]:1}
        max_len = 1
        j = 0   # j : end
        for i in range(len(nums)):   # i : start
            if i > 0:
                count_dict[nums[i-1]] -= 1
                if count_dict[nums[j]] > k:
                    continue
            while j < len(nums)-1:
                j += 1
                if count_dict.get(nums[j]):
                    count_dict[nums[j]] += 1
                else:
                    count_dict[nums[j]] = 1
                if count_dict[nums[j]] > k:
                    break
                else:
                    max_len = max(max_len, j-i+1)
        return max_len