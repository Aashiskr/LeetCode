class Solution(object):
    def getConcatenation(self, nums):
        l=len(nums)
        for i in range(l):
            nums.append(nums[i])
        return nums
        