class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit, islands = set(), 0
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #(0, 1) = "1"
        #(0,2), (0,0), (1, 1), (-1, 1)
        def bfs(r,c):
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == "1" and (new_r,new_c) not in visit:
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands