class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        atl = set()
        pac = set()
        rows = len(heights)
        cols = len(heights[0])
        def helper(i, j,visited,prev):
            if i < 0 or j < 0 or i == rows or j == cols or (i,j) in visited or heights[i][j] < prev:
                return
            
            visited.add((i,j))
            helper(i + 1, j, visited, heights[i][j])
            helper(i - 1,j, visited, heights[i][j])

            helper(i, j + 1, visited, heights[i][j])
            helper(i,j - 1, visited, heights[i][j])
        
        for c in range(cols):
            helper(0, c, pac, heights[0][c])
            helper(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            helper(r,0,pac,heights[r][0])
            helper(r,cols - 1,atl, heights[r][cols - 1])

        for x in range(rows):
            for y in range(cols):
                if (x,y) in pac and (x,y) in atl:
                    res.append([x,y])

        return res

