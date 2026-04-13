class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])


        # 1. Capture unsurrounded region
        def capture(r,c):
            if (r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0,ROWS - 1] or c in [0, COLS - 1])):
                    capture(r,c)
        
        # 2. Capture the surrounded regions (O -> Xs)
        for r in range(ROWS):
                    for c in range(COLS):
                        if board[r][c] == "O":
                            board[r][c] = "X"
        
        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
                    for c in range(COLS):
                        if board[r][c] == "T":
                            board[r][c] = "O"