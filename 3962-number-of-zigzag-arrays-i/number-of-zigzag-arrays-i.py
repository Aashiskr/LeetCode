class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        k = r - l + 1  # Total numbers available in our range
        
        # Edge cases 
        if k <= 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return (k * (k - 1)) % MOD
            
        # Base Case for length 2
        # Use 0-based indexing for values (0 to k-1)
        dp_up = [0] * k
        dp_down = [0] * k
        
        # For length 2, how many ways to reach value 'v' with UP or DOWN
        for v in range(k):
            dp_up[v] = v             # 'v' numbers are strictly smaller than 'v'
            dp_down[v] = k - 1 - v   # 'k-1-v' numbers are strictly greater than 'v'
            
        # Build up to length 'n'
        for length in range(3, n + 1):
            new_dp_up = [0] * k
            new_dp_down = [0] * k
            
            # Use Prefix Sum to calculate new_dp_up
            # new_dp_up[v] needs sum of dp_down from 0 to v-1
            pref_sum = 0
            for v in range(k):
                new_dp_up[v] = pref_sum
                pref_sum = (pref_sum + dp_down[v]) % MOD
                
            # Use Suffix Sum to calculate new_dp_down
            # new_dp_down[v] needs sum of dp_up from v+1 to k-1
            suff_sum = 0
            for v in range(k - 1, -1, -1):
                new_dp_down[v] = suff_sum
                suff_sum = (suff_sum + dp_up[v]) % MOD
                
            # Move to the next length iteration
            dp_up = new_dp_up
            dp_down = new_dp_down
            
        # Final answer is the sum of all valid configurations of length n
        total_valid_arrays = (sum(dp_up) + sum(dp_down)) % MOD
        
        return total_valid_arrays