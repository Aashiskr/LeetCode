class Solution(object):
    def minimumDifference(self, nums, k):
        # Agar sirf 1 element pick karna hai, toh highest - lowest hamesha 0 hoga
        if k == 1:
            return 0
            
        nums.sort()  # Array ko chhote se bade mein sort kiya
        min_diff = float('inf')  # Shuru mein difference ko infinity set kar diya
        
        # Sliding window lagayenge jiska size k hai
        # Loop wahan tak chalega jahan tak k size ki window ban sakti hai
        for i in range(len(nums) - k + 1):
            # Window ka highest element: nums[i + k - 1]
            # Window ka lowest element: nums[i]
            current_diff = nums[i + k - 1] - nums[i]
            
            # Agar current difference pichle minimum se kam hai, toh update karo
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff