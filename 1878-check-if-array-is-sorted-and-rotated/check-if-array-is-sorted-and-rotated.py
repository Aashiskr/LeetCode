class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Compare current element with the next element (wrapping around using modulo)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
            # If we find more than one drop, it can't be a sorted and rotated array
            if count > 1:
                return False
                
        return True