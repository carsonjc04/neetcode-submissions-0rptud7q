class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visit = set()
        islands = 0


        def dfs(r,c):
            # Find how big this island is, mark each with visited
            for dr, dc in directions:
                curRow, curCol = r + dr, c + dc
                if curRow in range(ROWS) and curCol in range(COLS) and (curRow, curCol) not in visit and grid[curRow][curCol] == "1":
                    visit.add((curRow, curCol))
                    dfs(curRow, curCol)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    visit.add((r,c))
                    dfs(r,c)
                    islands += 1
        
        return islands