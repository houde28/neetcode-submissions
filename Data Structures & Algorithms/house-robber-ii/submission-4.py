class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache1 = [-1] * n
        cache2 = [-1] * n
        if n == 1:
            return nums[0]
        def dfs(i,direction):
            if direction == 1:
                if i >= n-1:
                    return 0
                if cache1[i] != -1:
                    return cache1[i]
                cache1[i] = max(nums[i]+dfs(i+2,1),dfs(i+1,1))
                return cache1[i]
            else:
                if i >= n:
                    return 0
                if cache2[i] != -1:
                    return cache2[i]
                cache2[i] = max(nums[i] + dfs(i+2,-1), dfs(i+1,-1))
                return cache2[i]

            
        return max(dfs(0,1),dfs(1,-1))