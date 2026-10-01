class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def helper(char,index1,index2):
            if index1 >= len(board) or index1 < 0:
                return False
                
            if index2 >= len(board[0]) or index2 < 0:
                return False
            
            if (index1, index2) in seen:
                return False

            if board[index1][index2] == word[char]:
                if char == len(word) - 1:
                    return True
                seen.add((index1, index2))
                right = helper(char+1, index1 + 1, index2)
                left = helper(char+1, index1 - 1, index2)
                up = helper(char+1, index1, index2 + 1)
                down = helper(char+1, index1, index2 - 1)
                seen.remove((index1, index2))

                return right or left or up or down

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(0,i,j):
                    return True
                else:
                    seen = set()
                    continue
    
        return False


    
