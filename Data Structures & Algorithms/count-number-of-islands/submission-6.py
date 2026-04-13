class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    r2, c2 = row + dr, col + dc
                    if r2 in range(ROWS) and c2 in range(COLS) and grid[r2][c2] == "1" and (r2,c2) not in visit:
                        q.append((r2,c2))
                        visit.add((r2, c2))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands

        