class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def dfs(r,c):
            if (r in range(ROWS) 
                and c in range(COLS) 
                and grid[r][c] == 1 
                and (r,c) not in visit):
                    visit.add((r,c))
                    return (1 + dfs(r, c + 1) +
                    dfs(r, c - 1) +
                    dfs(r + 1, c) +
                    dfs(r - 1, c))
            else:
                return 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, dfs(r,c))
        return area
