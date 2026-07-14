class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Precompute the GCD table for all numbers up to 200 to save time on function calls
        gcd_table = [[0] * 201 for _ in range(201)]
        
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        for i in range(201):
            for j in range(201):
                gcd_table[i][j] = compute_gcd(i, j)
                
        # dp dictionary maps (gcd_of_seq1, gcd_of_seq2) to the number of combinations
        # 0 represents an empty sequence
        dp = {(0, 0): 1}
        
        for x in nums:
            # Copy previous states to account for Choice 1: Ignoring the current number 'x'
            new_dp = dp.copy()
            
            for (g1, g2), ways in dp.items():
                
                # Choice 2: Add 'x' to seq1
                # If seq1 is empty (g1 == 0), the new gcd is just x. Otherwise, it's gcd(g1, x)
                ng1 = gcd_table[g1][x]
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + ways) % MOD
                
                # Choice 3: Add 'x' to seq2
                # If seq2 is empty (g2 == 0), the new gcd is just x. Otherwise, it's gcd(g2, x)
                ng2 = gcd_table[g2][x]
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + ways) % MOD
                
            dp = new_dp
            
        ans = 0
        # We look for all states where g1 == g2 and they are strictly greater than 0
        # (This naturally enforces the constraint that both subsequences are non-empty)
        for g in range(1, 201):
            if (g, g) in dp:
                ans = (ans + dp[(g, g)]) % MOD
                
        return ans