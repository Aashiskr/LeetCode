class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        
        for num in nums:
            # If we find a new maximum, the old maximum becomes the second maximum
            if num >= max1:
                max2 = max1
                max1 = num
            # If it's not greater than max1 but is greater than max2, update max2
            elif num > max2:
                max2 = num
                
        return (max1 - 1) * (max2 - 1)