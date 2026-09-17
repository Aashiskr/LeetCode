class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        last_end = -1  # End index of the last chosen non-overlapping palindrome
        
        for i in range(n):
            # Check length k palindrome ending at index i
            if i - k + 1 > last_end:
                sub = s[i - k + 1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    continue
            
            # Check length k + 1 palindrome ending at index i
            if i - k > last_end:
                sub = s[i - k : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    
        return ans