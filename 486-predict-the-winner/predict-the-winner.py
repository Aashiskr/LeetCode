class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # dp[i][j] stores the maximum score difference the current player 
        # can get from the subarray nums[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: if there is only one element left, the player takes it
        for i in range(n):
            dp[i][i] = nums[i]
            
        # Build the DP table for subarray lengths from 2 up to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # The current player takes the left or right element, 
                # minus the optimal difference the opponent will get from the remainder.
                take_left = nums[i] - dp[i + 1][j]
                take_right = nums[j] - dp[i][j - 1]
                
                dp[i][j] = max(take_left, take_right)
                
        # Player 1 wins or ties if their final score difference >= 0
        return dp[0][n - 1] >= 0