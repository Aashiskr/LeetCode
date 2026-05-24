class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * n  # Memoization array
        
        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            
            max_jumps = 1
            
            # Jump right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            # Jump left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            dp[i] = max_jumps
            return dp[i]
        
        # Try starting from every index and find the global maximum
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans