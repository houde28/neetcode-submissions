class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        index =(left+right)//2
        while left <= right:
            if nums[index] == target:
                return index
            elif target > nums[index]:
                left= index+1
            elif target < nums[index]:
                right = index-1
            index= (left+right)//2
        return -1