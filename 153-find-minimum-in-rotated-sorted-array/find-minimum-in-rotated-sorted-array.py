class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        # Binary search loop
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is at mid or in the left half.
            else:
                right = mid
                
        # When left == right, it points to the minimum element.
        return nums[left]