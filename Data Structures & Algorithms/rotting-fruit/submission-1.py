from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
        count = 0
        while queue:

            q_len = len(queue)
            for i in range(q_len):
                x, y = queue.popleft()

                if (x-1 >= 0 and grid[x-1][y] == 1):
                    grid[x-1][y] = 2
                    queue.append((x-1, y))
                
                if (x+1 < rows and grid[x+1][y] == 1):
                    grid[x+1][y] = 2
                    queue.append((x+1, y))

                if (y-1 >= 0 and grid[x][y-1] == 1):
                    grid[x][y-1] = 2
                    queue.append((x, y-1))
                
                if (y+1 < cols and grid[x][y+1] == 1):
                    grid[x][y+1] = 2
                    queue.append((x, y+1))
                
            if queue:
                count += 1
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return count