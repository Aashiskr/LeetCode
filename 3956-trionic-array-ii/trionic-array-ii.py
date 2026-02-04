class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)
        if n < 4: return 0
        
        # 1. left_max_inc[i]: Max sum of strictly increasing subarray ending at i (len >= 2)
        # Condition: l < p
        left_max_inc = [float('-inf')] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # Option: [nums[i-1], nums[i]] OR [left_max_inc[i-1] + nums[i]]
                left_max_inc[i] = max(nums[i-1] + nums[i], left_max_inc[i-1] + nums[i])

        # 2. right_max_inc[i]: Max sum of strictly increasing subarray starting at i (len >= 2)
        # Condition: q < r
        right_max_inc = [float('-inf')] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                # Option: [nums[i], nums[i+1]] OR [nums[i] + right_max_inc[i+1]]
                right_max_inc[i] = max(nums[i] + nums[i+1], nums[i] + right_max_inc[i+1])

        max_trionic = float('-inf')
        
        # 3. Best (Peak + Decreasing Middle)
        # current_peak_path will store the max sum of (Left Wing + Decreasing sequence)
        current_peak_path = float('-inf')

        for i in range(1, n - 1):
            # Potential peak at i-1
            peak_val = left_max_inc[i-1]
            
            # If the sequence is decreasing
            if nums[i] < nums[i-1]:
                # We can either start a NEW decreasing sequence from peak i-1
                # OR continue the existing best_peak_path by adding nums[i]
                option_start_new = peak_val + nums[i] if peak_val != float('-inf') else float('-inf')
                option_continue = current_peak_path + nums[i] if current_peak_path != float('-inf') else float('-inf')
                
                current_peak_path = max(option_start_new, option_continue)
                
                # If current_peak_path is valid and i is a valid valley (has right wing)
                if current_peak_path != float('-inf') and right_max_inc[i] != float('-inf'):
                    # Sum = (Left Wing + Middle ending at i) + (Right Wing starting at i)
                    # Note: nums[i] is in both current_peak_path and right_max_inc[i], so subtract once.
                    max_trionic = max(max_trionic, current_peak_path + right_max_inc[i] - nums[i])
            else:
                # Sequence is not decreasing, reset the path
                current_peak_path = float('-inf')

        return int(max_trionic)