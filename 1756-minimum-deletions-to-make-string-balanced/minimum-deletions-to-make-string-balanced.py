class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_count = 0
        min_deletions = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                # If we encounter an 'a' and we have seen 'b's previously,
                # it's a violation. We either delete this 'a' or one of the previous 'b's.
                # Greedy choice: increment deletion count and decrease b_count
                # (effectively removing the pair that causes the violation).
                if b_count > 0:
                    min_deletions += 1
                    b_count -= 1
                    
        return min_deletions