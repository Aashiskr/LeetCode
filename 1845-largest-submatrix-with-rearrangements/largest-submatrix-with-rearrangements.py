from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Step 1: Accumulate heights column by column
        for i in range(m):
            for j in range(n):
                # If the current cell is 1 and it's not the first row, 
                # add the height of consecutive 1s from the row above
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
        
        # Step 2 & 3: Sort each row and calculate max area
        for i in range(m):
            # Sort the heights in the current row in descending order
            curr_row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                # If the height is 0, any subsequent width will also yield 0 area
                if curr_row[j] == 0:
                    break
                
                # Area = height * width
                area = curr_row[j] * (j + 1)
                if area > max_area:
                    max_area = area
                    
        return max_area