class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
            
        # Find the indices of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Identify the smaller and larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Calculate the three possible strategies
        both_from_front = j + 1
        both_from_back = n - i
        one_front_one_back = (i + 1) + (n - j)
        
        # Return the minimum deletions required
        return min(both_from_front, both_from_back, one_front_one_back)