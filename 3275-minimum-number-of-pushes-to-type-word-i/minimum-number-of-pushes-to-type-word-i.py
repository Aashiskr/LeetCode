class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        total_pushes = 0
        
        for i in range(n):
            # i // 8 gives the 0-indexed position (0 for 1st, 1 for 2nd, etc.)
            # Add 1 to get the actual number of pushes required
            total_pushes += (i // 8) + 1
            
        return total_pushes