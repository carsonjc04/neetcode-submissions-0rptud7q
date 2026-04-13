class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r,new_c))
            time += 1
        
        return time if fresh == 0 else -1