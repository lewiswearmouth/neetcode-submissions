class Solution:
    # O(n^2) time and O(n^2) space
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        duplicate_row = collections.defaultdict(set)
        duplicate_col = collections.defaultdict(set)
        duplicate_square = collections.defaultdict(set) # key = (r/3, c/3)
        
        for r in range(len(board)): 
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in duplicate_row[r] or board[r][c] in duplicate_col[c] or board[r][c] in duplicate_square[r//3,c//3]):
                  return False
                duplicate_col[c].add(board[r][c])
                duplicate_row[r].add(board[r][c])
                duplicate_square[r//3,c//3].add(board[r][c])
        return True
                
        