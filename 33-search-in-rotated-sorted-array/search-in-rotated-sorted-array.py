class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Target found
            if nums[mid] == target:
                return mid
            
            # Check if the left half is strictly sorted
            if nums[left] <= nums[mid]:
                # If target is within the bounds of the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is on the left
                else:
                    left = mid + 1   # Target is on the right
                    
            # Otherwise, the right half must be strictly sorted
            else:
                # If target is within the bounds of the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is on the right
                else:
                    right = mid - 1  # Target is on the left
                    
        # Target not found
        return -1