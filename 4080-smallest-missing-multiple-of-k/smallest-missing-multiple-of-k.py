class Solution(object):
    def missingMultiple(self, nums, k):
        x=k
        while(k in nums):
            k=k+x
        return k