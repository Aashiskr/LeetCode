from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Calculate the 2D prefix sum in-place
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                
                # Check if the current submatrix sum is within the limit
                if grid[i][j] <= k:
                    count += 1
                else:
                    # If the first element in the row is already > k, 
                    # no subsequent rows will be valid either.
                    if j == 0:
                        return count
                    
                    # Since all numbers are >= 0, moving further right 
                    # will only increase the sum, so we can skip the rest of this row.
                    break 
                    
        return count