class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {}
        n = len(nums)
        
        # Iterate through every possible subarray of size k
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            
            # Use a set to only count an element once per subarray
            unique_elements = set(subarray)
            for num in unique_elements:
                counts[num] = counts.get(num, 0) + 1
                
        # Find the largest integer that appears in exactly one subarray
        largest_almost_missing = -1
        for num, count in counts.items():
            if count == 1:
                if num > largest_almost_missing:
                    largest_almost_missing = num
                    
        return largest_almost_missing