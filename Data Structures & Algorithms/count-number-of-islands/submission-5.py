class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    nxt_r, nxt_c = row + dr, col + dc
                    if nxt_r in range(ROWS) and nxt_c in range(COLS) and grid[nxt_r][nxt_c] == "1" and (nxt_r, nxt_c) not in visit:
                        q.append((nxt_r, nxt_c))
                        visit.add((nxt_r, nxt_c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        
        return island
                
