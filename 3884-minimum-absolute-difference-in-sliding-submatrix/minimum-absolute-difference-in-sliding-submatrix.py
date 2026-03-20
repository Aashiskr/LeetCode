from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Initialize the result matrix
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Extract unique values from the current k x k submatrix
                unique_vals = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        unique_vals.add(grid[r][c])
                
                # If there are no two distinct values, the answer is 0
                if len(unique_vals) < 2:
                    ans[i][j] = 0
                else:
                    # Sort the unique values and check adjacent elements
                    sorted_vals = sorted(unique_vals)
                    min_diff = min(sorted_vals[x] - sorted_vals[x - 1] for x in range(1, len(sorted_vals)))
                    ans[i][j] = min_diff
                    
        return ans