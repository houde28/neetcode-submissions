class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row=0
        right_row=len(matrix)-1
        left_col= 0
        right_col = len(matrix[0])-1
        while left_row <= right_row:
            row_index = (left_row + right_row)//2
            if target >= matrix[row_index][0] and target <= matrix[row_index][-1]:
                col_index= (left_col + right_col)//2
                while left_col <= right_col:
                    if matrix[row_index][col_index] == target:
                        return True
                    elif target > matrix[row_index][col_index] :
                        left_col = col_index + 1
                    elif target < matrix[row_index][col_index]:
                        right_col = col_index -1
                    
                    col_index= (left_col + right_col)//2
                if matrix[row_index][col_index] != target:
                    return False
            elif target > matrix[row_index][0]:
                left_row = row_index + 1
            else:
                right_row = row_index - 1
            
        return False