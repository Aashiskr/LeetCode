class Solution(object):
    def finalPrices(self, prices):
        l = len(prices)
        nums=prices
        for i in range(l):
            for j in range(i+1,l,1):
                if(nums[i]>=nums[j]):
                    nums[i]=nums[i]-nums[j]
                    break
        return nums