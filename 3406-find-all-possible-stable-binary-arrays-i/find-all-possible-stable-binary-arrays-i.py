class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base Cases: Arrays consisting entirely of 0s or entirely of 1s
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
            
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # Fill the DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # Calculate ways to end with 0
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # Subtract invalid cases exceeding the limit
                    dp[i][j][0] = (dp[i][j][0] - dp[i - 1 - limit][j][1] + MOD) % MOD
                
                # Calculate ways to end with 1
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # Subtract invalid cases exceeding the limit
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - limit][0] + MOD) % MOD
                    
        # Total valid arrays using exactly 'zero' 0s and 'one' 1s
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD