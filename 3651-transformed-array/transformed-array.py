class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize the result array with the same length
        result = [0] * n
        
        for i in range(n):
            # Calculate the landing index. 
            # (i + nums[i]) % n handles right, left, and zero movement.
            target_index = (i + nums[i]) % n
            result[i] = nums[target_index]
            
        return result