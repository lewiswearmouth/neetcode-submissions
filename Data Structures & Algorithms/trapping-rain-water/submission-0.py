class Solution:
    def trap(self, height: List[int]) -> int:
        # formula: min(max_left, max_right) - height[i]
        max_left = [0] * len(height)
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])

        max_right = [0] * len(height)
        max_right[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
        
        area = 0 
        for i in range(len(height)):
            if height[i] < min(max_left[i], max_right[i]):
                area += min(max_left[i], max_right[i]) - height[i]
        
        return area