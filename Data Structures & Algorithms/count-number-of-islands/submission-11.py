class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                for dr, dc in directions:
                    row2, col2 = row + dr, col + dc
                    if row2 in range(ROWS) and col2 in range(COLS) and (row2, col2) not in visited and grid[row2][col2] == "1":
                        visited.add((row2, col2))
                        q.append((row2, col2))
                        



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
        