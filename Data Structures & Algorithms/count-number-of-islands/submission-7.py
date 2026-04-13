class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        island = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()

        def bfs(r,c):
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r2, c2 = row + dr, col + dc
                    if r2 in range(ROWS) and c2 in range(COLS) and grid[r2][c2] == "1" and (r2,c2) not in visited:
                        q.append((r2,c2))
                        visited.add((r2,c2))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        return island

