class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        def dfs(r,c):
            visited.add((r,c))
            for dr, dc in directions:
                r2, c2 = r + dr, c + dc
                if r2 in range(ROWS) and c2 in range(COLS) and (r2, c2) not in visited and grid[r2][c2] == "1":
                    dfs(r2,c2)
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands
        