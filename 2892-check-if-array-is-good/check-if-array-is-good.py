class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        
        # A 'good' array base[n] must have at least 2 elements ([1, 1])
        if n < 1:
            return False
        
        # Sort the array to check the permutation easily
        nums.sort()
        
        # Check elements 1 to n-1
        for i in range(n):
            if nums[i] != i + 1:
                return False
        
        # Check if the last element is also n
        return nums[n] == n