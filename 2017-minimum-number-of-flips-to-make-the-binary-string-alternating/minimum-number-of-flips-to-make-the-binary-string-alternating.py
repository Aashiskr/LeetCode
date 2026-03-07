class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        s = s + s  # Double the string to handle circular shifts
        
        # Create our two alternating target patterns
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += '1' if i % 2 == 0 else '0'
            target2 += '0' if i % 2 == 0 else '1'
            
        ans = float('inf')
        diff1, diff2 = 0, 0
        l = 0
        
        # Sliding window
        for r in range(len(s)):
            # If the current character doesn't match the target, we need a flip
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
                
            # If our window has exceeded the original string length, shrink it from the left
            if r - l + 1 > n:
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
                
            # Once our window is exactly size n, we can record the minimum flips
            if r - l + 1 == n:
                ans = min(ans, diff1, diff2)
                
        return ans