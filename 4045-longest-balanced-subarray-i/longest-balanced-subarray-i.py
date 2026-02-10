class Solution(object):
    def longestBalanced(self, nums):
        max_len = 0
        n = len(nums)
        
        # Check every possible starting point
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Extend the subarray from the starting point i
            for j in range(i, n):
                num = nums[j]
                
                # Add to the appropriate set
                if num % 2 == 0:
                    distinct_evens.add(num)
                else:
                    distinct_odds.add(num)
                
                # If balanced, update max_len
                if len(distinct_evens) == len(distinct_odds):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len