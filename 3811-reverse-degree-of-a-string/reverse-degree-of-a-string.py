class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_degree = 0
        
        for i, char in enumerate(s, 1):
            # Calculate the reversed alphabet value (a=26, b=25, ..., z=1)
            reversed_val = 26 - (ord(char) - ord('a'))
            
            # Multiply by the 1-based index and add to the total
            total_degree += reversed_val * i
            
        return total_degree