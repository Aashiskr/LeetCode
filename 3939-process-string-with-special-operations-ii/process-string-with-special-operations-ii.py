class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        
        # Step 1: Precompute string lengths at each step
        L = [0] * n
        curr_len = 0
        
        for i in range(n):
            ch = s[i]
            if ch == '*':
                curr_len = max(0, curr_len - 1)
            elif ch == '#':
                curr_len *= 2
            elif ch == '%':
                pass # Length remains unchanged
            else:
                curr_len += 1
            L[i] = curr_len
            
        # If k is out of bounds for the final resulting string
        if k >= L[-1]:
            return "."
            
        # Step 2: Traverse backwards to trace the character at index k
        idx = k
        for i in range(n - 1, -1, -1):
            # Length of the string immediately before the current operation
            prev_len = L[i-1] if i > 0 else 0
            ch = s[i]
            
            if ch == '*':
                # Backspace simply removes the last char, so the target idx is unaffected
                pass
            elif ch == '#':
                # Re-map index to the original half before duplication
                idx %= prev_len
            elif ch == '%':
                # Re-map index to its original position before the reversal
                idx = prev_len - 1 - idx
            else:
                # If it's a character, it was appended precisely at index `prev_len`
                if idx == prev_len:
                    return ch
        
        return "."