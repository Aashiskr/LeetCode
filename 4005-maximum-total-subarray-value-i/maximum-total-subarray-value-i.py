class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Find the overall maximum and minimum values in the array
        max_val = max(nums)
        min_val = min(nums)
        
        # The maximum possible value for a single subarray
        max_subarray_value = max_val - min_val
        
        # Multiply by k since we can just pick this optimal subarray k times
        return max_subarray_value * k