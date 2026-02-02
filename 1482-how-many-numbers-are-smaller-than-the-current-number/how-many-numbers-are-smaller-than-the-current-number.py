class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = len(nums)
        num = []
        x = 0
        for i in range(l):
            x = 0
            for j in range(l):
                if(nums[i]>nums[j]):
                    x = x+1
            num.append(x)
        return num
        