class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 rules we need to meet. All of them are duplicates. We can solve this with sets. Specifically defaultdict(set())
        ROWS, COLS, GRID = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in ROWS[r] or board[r][c] in COLS[c] or board[r][c] in GRID[r//3,c//3]:
                    return False
        
                ROWS[r].add(board[r][c])
                COLS[c].add(board[r][c])
                GRID[r//3, c//3].add(board[r][c])
        return True

