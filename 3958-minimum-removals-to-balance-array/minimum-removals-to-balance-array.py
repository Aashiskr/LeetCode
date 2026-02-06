class Solution(object):
    def minRemoval(self, nums, k):
        # 1. Sabse pehle sort karna zaroori hai!
        nums.sort() 
        
        max_window = 0
        left = 0
        n = len(nums)
        
        for right in range(n):
            # 2. Jab tak condition satisfy nahi hoti, left ko badhao
            while nums[right] > nums[left] * k:
                left += 1
            
            # 3. Maximum valid window size update karo
            max_window = max(max_window, right - left + 1)

        # 4. Total mein se max_window minus karo
        return n - max_window