class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        amount = 0
        length = len(cost)
        cache = [-1]*length
        def dfs(i):
            if i >= length:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = min((dfs(i+2)+cost[i]),(dfs(i+1)+cost[i]))
            return cache[i]

        return min(dfs(0),dfs(1))