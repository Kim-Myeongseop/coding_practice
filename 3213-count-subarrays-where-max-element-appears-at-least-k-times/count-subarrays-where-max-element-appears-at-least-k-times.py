class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        l, cnt, result = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == max_num:
                cnt += 1
            while cnt >= k:
                if nums[l] == max_num:
                    cnt -= 1
                l += 1
            result += l
        return result