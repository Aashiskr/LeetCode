class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Case 1: The minimum element is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            
            # Case 2: The minimum element is in the left half (including mid)
            elif nums[mid] < nums[high]:
                high = mid
            
            # Case 3: Duplicates encountered (nums[mid] == nums[high])
            # We cannot confidently discard either half, so we safely shrink the search space.
            else:
                high -= 1
                
        return nums[low]