class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]
        for i in range(9):
            seen =set()
            seen_col=set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                
                    seen.add(board[i][j])
                    square = (i //3)*3 + (j // 3)

                    if board[i][j] in squares[square]:
                        return False
                    squares[square].add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])
                

        return True