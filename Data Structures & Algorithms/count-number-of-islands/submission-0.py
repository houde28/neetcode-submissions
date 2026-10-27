class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = set()
        res = 0

        def helper(x,y):
            if (x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == "0" or (x,y) in island):
                return False
            island.add((x,y))
            helper(x + 1, y)
            helper(x - 1, y)
            helper(x, y + 1)
            helper(x, y - 1)
            
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if helper(i,j):
                    res += 1
        
        return res
