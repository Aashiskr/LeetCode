class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        
        # Two pointers: one starting from left (for elements < pivot)
        # one starting from right (for elements > pivot)
        left = 0
        right = n - 1
        
        # Traverse from left to right for elements smaller than pivot
        for i in range(n):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
                
        # Traverse from right to left for elements greater than pivot
        # We read nums backwards to maintain the relative order when placing at the back
        for i in range(n - 1, -1, -1):
            if nums[i] > pivot:
                ans[right] = nums[i]
                right -= 1
                
        # Fill the remaining middle slots with the pivot
        while left <= right:
            ans[left] = pivot
            left += 1
            
        return ans