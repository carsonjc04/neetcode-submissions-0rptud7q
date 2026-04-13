class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        directions = [[1,0], [-1,0], [0,-1], [0,1]]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS or (new_r,new_c) in visit or grid[new_r][new_c] == -1):
                        continue
                    else:
                        visit.add((new_r,new_c))
                        q.append((new_r,new_c))
                    
            dist += 1
                


