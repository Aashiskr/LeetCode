class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Find all indices of '1's in the string
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # If there are fewer than k ones in total, no beautiful substring is possible
        if len(ones) < k:
            return ""
        
        best_str = ""
        
        # Check every window of exactly k ones
        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            
            # Substring spanning exactly k ones (no extra leading/trailing zeros)
            cand = s[left:right+1]
            
            # If we don't have a best string yet, or the candidate is shorter
            if not best_str or len(cand) < len(best_str):
                best_str = cand
            # If there's a tie in length, take the lexicographically smallest one
            elif len(cand) == len(best_str):
                best_str = min(best_str, cand)
                
        return best_str