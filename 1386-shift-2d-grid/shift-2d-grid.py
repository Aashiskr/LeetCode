class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # Optimize k in case it's larger than the total number of elements
        k = k % total_elements
        
        # If k is 0, the grid remains exactly the same
        if k == 0:
            return grid
            
        # Initialize a new grid with zeros
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Calculate new 1D index
                new_1d_index = (r * n + c + k) % total_elements
                
                # Convert back to 2D coordinates
                new_r = new_1d_index // n
                new_c = new_1d_index % n
                
                # Place the element in the new grid
                result[new_r][new_c] = grid[r][c]
                
        return result