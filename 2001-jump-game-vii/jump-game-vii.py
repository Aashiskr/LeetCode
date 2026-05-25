class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # If the destination is '1', it's impossible to reach.
        if s[-1] == '1':
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        # Tracks the number of reachable indices we can currently jump from
        available_jumps = 0
        
        for i in range(1, n):
            # When an index is at least minJump away, it enters our valid jump window
            if i >= minJump and dp[i - minJump]:
                available_jumps += 1
                
            # When an index is further than maxJump away, it leaves our valid jump window
            if i > maxJump and dp[i - maxJump - 1]:
                available_jumps -= 1
                
            # We can reach index i if it's '0' and we have at least one valid jump off point
            if s[i] == '0' and available_jumps > 0:
                dp[i] = True
                
        return dp[-1]