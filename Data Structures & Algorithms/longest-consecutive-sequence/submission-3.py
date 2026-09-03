class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest= 0
        seen=set(nums)
        for x in seen:
            if x-1 not in seen:
                current = x
                count=1
                while current + 1 in seen:
                    current +=1
                    count +=1
                if count > longest:
                    longest = count
            
       
        
        return longest



            