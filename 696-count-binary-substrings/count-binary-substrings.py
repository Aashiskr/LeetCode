class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        count = 1
        
        # 1. Groups banao
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        
        # 2. Minimum nikaal kar total karo
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i], groups[i-1])
            
        return ans