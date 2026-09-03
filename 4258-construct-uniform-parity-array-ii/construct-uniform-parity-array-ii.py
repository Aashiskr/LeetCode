class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Find the absolute minimum element in the array
        min_val = min(nums1)
        
        # If the minimum element is odd, we can always make all elements odd
        if min_val % 2 != 0:
            return True
            
        # If the minimum element is even, we can't have ANY odd elements
        for num in nums1:
            if num % 2 != 0:
                return False
                
        return True