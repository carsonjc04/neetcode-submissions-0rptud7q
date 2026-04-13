class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0,0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    r2 = r + dr
                    c2 = c + dc
                    if r2 not in range(ROWS) or c2 not in range(COLS) or grid[r2][c2] != 1:
                        continue
                    grid[r2][c2] = 2
                    q.append([r2,c2])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1