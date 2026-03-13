import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        min_w = min(workerTimes)
        
        # Binary search bounds
        low = 1
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            total_height_reduced = 0
            # Check how much height all workers can reduce in 'mid' seconds
            for w in workerTimes:
                # Using the quadratic formula to find max height 'x' for this worker
                K = (2 * mid) // w
                
                # Replaced math.isqrt with int(math.sqrt()) for older Python versions
                x = (int(math.sqrt(1 + 4 * K)) - 1) // 2
                
                total_height_reduced += x
                
                # Early exit if we've already reached the target height
                if total_height_reduced >= mountainHeight:
                    break
            
            if total_height_reduced >= mountainHeight:
                ans = mid       # This time works, record it
                high = mid - 1  # Try to find a smaller time
            else:
                low = mid + 1   # We need more time
                
        return ans