class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # The maximum possible sum is 2 * limit. 
        # We need an array up to 2 * limit + 2 to handle the upper boundary safely.
        delta = [0] * (2 * limit + 2)
        
        # Process each pair from the outside in
        for i in range(n // 2):
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])
            
            # Boundary updates based on the sweep-line logic
            delta[2] += 2                 # Start with 2 moves at minimum possible sum
            delta[A + 1] -= 1             # Drops to 1 move
            delta[A + B] -= 1             # Drops to 0 moves
            delta[A + B + 1] += 1         # Increases to 1 move
            delta[B + limit + 1] += 1     # Increases to 2 moves
            
        min_moves = float('inf')
        current_moves = 0
        
        # Calculate prefix sums to find the optimal target T that minimizes moves
        for T in range(2, 2 * limit + 1):
            current_moves += delta[T]
            if current_moves < min_moves:
                min_moves = current_moves
                
        return min_moves