class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Approach:
        # we will create a set for each row and col. for boxes we can create
        # a set, but how will we know which to put it in? we can use a //3 to 
        # now we iterate through, skipping "." if board[r][c] in row, col, or square return fals
        # otherwise, add value to sets and finish iteration

        ROWS, COLS, SQUARES = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in ROWS[r] or board[r][c] in COLS[c] or board[r][c] in SQUARES[r//3, c//3]:
                    return False
                ROWS[r].add(board[r][c])
                COLS[c].add(board[r][c])
                SQUARES[r//3, c//3].add(board[r][c])
        return True