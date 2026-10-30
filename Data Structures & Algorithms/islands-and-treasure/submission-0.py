from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            x, y = queue.popleft()
                
            if x - 1 >= 0:
                if grid[x - 1][y] == 2147483647:
                    grid[x-1][y] = grid[x][y] + 1
                    queue.append((x-1,y))
                
            if x + 1 < len(grid):
                if grid[x + 1][y] == 2147483647:
                    grid[x+1][y] = grid[x][y] + 1
                    queue.append((x+1,y))
                
            if y + 1 < len(grid[0]):
                if grid[x][y+1] == 2147483647:
                    grid[x][y+1] = grid[x][y] + 1
                    queue.append((x,y+1))
                
            if y - 1 >= 0:
                if grid[x][y-1] == 2147483647:
                    grid[x][y-1] = grid[x][y] + 1
                    queue.append((x,y-1))
            
                