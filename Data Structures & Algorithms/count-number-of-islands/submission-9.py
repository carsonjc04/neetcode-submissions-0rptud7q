class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()            
                for dr, dc in directions:
                    row2, col2 = dr + row, dc + col
                    if row2 in range(ROWS) and col2 in range(COLS) and grid[row2][col2] == "1" and (row2, col2) not in visited:
                        q.append((row2, col2))
                        visited.add((row2, col2))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
