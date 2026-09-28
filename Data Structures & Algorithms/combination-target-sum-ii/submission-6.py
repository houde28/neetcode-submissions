class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def dfs(cur_list, cur_sum, cur):
            if cur_sum == target:
                res.append(cur_list.copy())
                return
            
            if cur >= len(candidates) or cur_sum > target:
                return
            
            cur_list.append(candidates[cur])
            dfs(cur_list,cur_sum+candidates[cur],cur+1)
            cur_list.pop()
            while cur + 1 < len(candidates) and candidates[cur+1] == candidates[cur]:
                cur += 1
            dfs(cur_list, cur_sum,cur+1)

        dfs([], 0, 0)
        return res
