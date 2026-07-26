class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        
        # Scenario 1: Top 3 largest numbers
        opt1 = nums[-1] * nums[-2] * nums[-3]
        
        # Scenario 2: 2 smallest numbers (most negative) * largest number
        opt2 = nums[0] * nums[1] * nums[-1]
        
        return max(opt1, opt2)