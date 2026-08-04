class Solution(object):
    def findMissingElements(self, nums):
        a=min(nums)
        b=max(nums)
        x=[]

        for i in range(a,b,1):
            if i not in nums:
                x.append(i)
        return x

        