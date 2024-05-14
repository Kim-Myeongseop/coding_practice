class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        total = len1 + len2
        half = (total+1) // 2   # 3 -> 2 : total이 홀수일 때, 중간 값 포함
        l = 0
        r = len1   # len1-1로 설정하면 len1 = 0 일때, while문이 돌지 않음.
        while l <= r:
            m1 = (l+r)//2   # len1 = 4, len2 = 5 라 하면, m1은 left subset1의 원소 개수를 의미
            m2 = half - m1   # 따라서, m2도 left subset2의 원소 개수를 의미 해야하므로 다음과 같다. 홀수일 때는 포함
            print(l, r)
            print(m1, m2)

            left_sup1 = float('-inf') if m1-1 == -1 else nums1[m1-1]   # if m1-1 == -1 이 더 직관적이어서 사용.
            left_sup2 = -float('inf') if m2-1 == -1 else nums2[m2-1]   # float('inf'), -float('inf') 모두 가능
            right_inf1 = float('inf') if m1 == len1 else nums1[m1]
            right_inf2 = float('inf') if m2 == len2 else nums2[m2]
            print(left_sup1, right_inf1)
            print(left_sup2, right_inf2)

            if left_sup1 <= right_inf2 and left_sup2 <= right_inf1:   # left_sup 끼리, right_inf 끼리 비교 남음
                if total%2 == 0:
                    return (max(left_sup1, left_sup2) + min(right_inf1, right_inf2)) / 2.0
                else:
                    return max(left_sup1, left_sup2)   # m1, m2는 개수이고, 합은 필요한 half이다.
            
            elif left_sup1 > right_inf2:
                r = m1 - 1
            
            else:   # left_sup1 <= right_inf2 and left_sup2 > right_inf1 : left_sup2가 right_inf1 보다도 크므로,
                l = m1 + 1   # l을 올리고, nums1에서 필요한 원소의 개수를 늘리고, nums2에서는 줄여여한다.
        
        return 326   # 형식상 필요