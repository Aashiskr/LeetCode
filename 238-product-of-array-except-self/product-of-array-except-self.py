class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        res = [1] * l

        prefix = 1
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(l - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
