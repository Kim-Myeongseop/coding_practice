
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height)-1
        result = [min(height[left_idx], height[right_idx]) * (right_idx - left_idx)]

        for i in range(len(height)-1):
            if height[left_idx] > height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1
            
            area = min(height[left_idx], height[right_idx]) * (right_idx - left_idx)
            result.append(area)
        return max(result)
                


            
        
                