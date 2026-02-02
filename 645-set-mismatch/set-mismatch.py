class Solution:
    def findErrorNums(self, nums):
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
            
        dup, missing = -1, -1
        
        # 1 se lekar n tak check karo
        for i in range(1, len(nums) + 1):
            count = counts.get(i, 0)
            if count == 2:
                dup = i
            elif count == 0:
                missing = i
        
        return [dup, missing]