class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(len(heights)):
            curr_height =  heights[i]
            next_index=None
            while stack and stack[-1][0] >= curr_height:
                next_height, next_index=stack.pop()
                width = i - next_index
                area = width * next_height
                if area > max_area:
                    max_area = area
            if next_index is None:
                stack.append((heights[i],i))
            else:
                stack.append((heights[i],next_index))
            
        while stack:
            curr_height, curr_index = stack.pop()
            width = len(heights) - curr_index
            area = curr_height * width
            if area > max_area:
                max_area = area
        return max_area
        
        
            
