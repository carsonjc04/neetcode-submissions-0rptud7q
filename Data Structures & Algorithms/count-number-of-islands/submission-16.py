class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
        def bfs(r,c):
            visit.add((r,c))
            q = collections.deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == "1" and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands