class Solution(object):
    def minimumCost(self, nums):
        m1=nums[0]
        nums.remove(m1)
        m2=min(nums)
        nums.remove(m2)
        m3=min(nums)
        nums.remove(m3)
        return m1+m2+m3
        