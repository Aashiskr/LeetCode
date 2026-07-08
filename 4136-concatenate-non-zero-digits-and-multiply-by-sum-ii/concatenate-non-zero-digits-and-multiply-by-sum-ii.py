class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)
        
        # Array to store powers of 10 modulo 10^9+7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # Prefix arrays initialize kar rahe hain
        pref_sum = [0] * (n + 1)
        pref_count = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        
        # Pre-computing the prefix arrays
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                pref_sum[i+1] = pref_sum[i] + digit
                pref_count[i+1] = pref_count[i] + 1
                pref_val[i+1] = (pref_val[i] * 10 + digit) % MOD
            else:
                # Agar 0 hai toh values same rahengi
                pref_sum[i+1] = pref_sum[i]
                pref_count[i+1] = pref_count[i]
                pref_val[i+1] = pref_val[i]
                
        ans = []
        
        # Har query ka answer O(1) time mein nikalna
        for L, R in queries:
            # Range [L, R] mein total non-zero digits kitne hain
            count = pref_count[R+1] - pref_count[L]
            
            # Agar range mein koi non-zero digit nahi hai
            if count == 0:
                ans.append(0)
                continue
            
            # Range [L, R] ke digits ka sum
            curr_sum = pref_sum[R+1] - pref_sum[L]
            
            # Substring ka number value nikalne ka formula
            val = (pref_val[R+1] - pref_val[L] * pow10[count]) % MOD
            
            # Final result modulo ke saath
            res = (val * curr_sum) % MOD
            ans.append(res)
            
        return ans