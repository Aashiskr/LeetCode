class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dp[i] will be True if the current player can win with i stones left
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            # Try removing every possible square number <= i
            for j in range(1, int(i**0.5) + 1):
                # If removing j*j stones leaves the opponent in a losing state, 
                # the current player wins.
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                    
        return dp[n]