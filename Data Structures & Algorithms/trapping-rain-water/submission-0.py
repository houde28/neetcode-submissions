class Solution:
    def trap(self, height: List[int]) -> int:
        water_amount = 0
        right = len(height)-1
        left= 0
        left_max=0
        right_max=0
        while left< right:
            if height[left] <= height[right]:
                current = left_max -height[left]
                if current >0:
                    water_amount += current
                left_max = max(left_max, height[left])
                left+=1
            else:
                current = right_max - height[right]
                if current > 0:
                    water_amount += current
                right_max = max(right_max, height[right])
                right -=1
                
        return water_amount