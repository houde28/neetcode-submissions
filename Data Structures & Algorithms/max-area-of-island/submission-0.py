class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island = set()
        res = 0
        big = 0

        def helper(x,y):
            if (x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0 or (x,y) in island):
                return 0
            island.add((x,y))
            return 1 + helper(x + 1, y) + helper(x - 1, y) + helper(x, y + 1) + helper(x, y - 1)
            
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in island:
                    cur = helper(i,j)
                    if cur > big:
                        big = cur
        
        return big