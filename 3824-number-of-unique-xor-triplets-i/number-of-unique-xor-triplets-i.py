class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Edge cases where n is 1 or 2
        if n < 3:
            return n
            
        # For n >= 3, calculate the next power of 2 based on the bit length of n
        return 1 << n.bit_length()