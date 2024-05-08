class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        low = 0
        high = len1
        left = (len1 + len2 + 1) // 2
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            l2 = -float('inf') if mid2 == 0 else nums2[mid2-1]
            r1 = math.inf if mid1 == len1 else nums1[mid1]
            r2 = math.inf if mid2 == len2 else nums2[mid2]
            if l1 <= r2 and l2 <= r1:
                if (len1 + len2) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0 