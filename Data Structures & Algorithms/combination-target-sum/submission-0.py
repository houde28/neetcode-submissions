class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur_list=[]
        def dfs(cur,cur_sum, cur_list):
            if cur_sum == target:
                res.append(cur_list.copy())
                return
            if cur >= len(nums) or cur_sum > target:
                return 
            
            cur_list.append(nums[cur])
            dfs(cur,cur_sum+nums[cur], cur_list)
            cur_list.pop()
            dfs(cur+1, cur_sum,cur_list)
            
        dfs(0,0,[])
        return res

        