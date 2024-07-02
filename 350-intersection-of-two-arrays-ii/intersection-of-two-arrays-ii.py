class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1_, nums2_ = nums1[:], nums2[:]
        for num in nums1_:
            if num in nums2_:
                answer.append(num)
                nums2_.remove(num)
        return answer