class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visted = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    row2, col2 = row + dr, col + dc
                    if row2 in range(ROWS) and col2 in range(COLS) and grid[row2][col2] == "1" and (row2,col2) not in visted:
                        q.append((row2,col2))
                        visted.add((row2,col2))



        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visted and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands