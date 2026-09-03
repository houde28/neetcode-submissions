class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        largest = 0
        while left < right:
            current_height = min(heights[left],heights[right]) * (right-left)
            if current_height > largest:
                largest = current_height
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return largest