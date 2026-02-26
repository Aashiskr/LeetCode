class Solution(object):
    def triangularSum(self, nums):
        n=len(nums)
        while n>1:
            for i in range(n-1):
                nums[i]=(nums[i]+nums[i+1])%10
            n=n-1
        return nums[0]

            


            
        