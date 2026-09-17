class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        min_len = [float('inf')] * n
        
        left = 0
        curr_sum = 0
        ans = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink window if current sum exceeds target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            # Found a subarray with sum equal to target
            if curr_sum == target:
                curr_len = right - left + 1
                
                # Check if there is a valid non-overlapping subarray to the left
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                # Update min_len for the current index
                min_len[right] = min(min_len[right - 1] if right > 0 else float('inf'), curr_len)
            else:
                # Carry forward the best length found so far
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')
                
        return ans if ans != float('inf') else -1