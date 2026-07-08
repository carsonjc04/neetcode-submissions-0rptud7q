class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        visit = set()
        islands = 0

        def bfs(r,c):

            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                r, c = q.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if ((row,col) not in visit 
                    and col in range(COLS) and row in range(ROWS) and grid[row][col] == "1"):
                        q.append((row,col))
                    
        

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
