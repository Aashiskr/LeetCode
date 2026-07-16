class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Helper function for Euclidean GCD to ensure cross-version compatibility
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        n = len(nums)
        prefixGcd = []
        
        # Step 1: Construct prefixGcd array in a single pass
        mx = 0
        for num in nums:
            if num > mx:
                mx = num
            prefixGcd.append(get_gcd(num, mx))
            
        # Step 2: Sort the array
        prefixGcd.sort()
        
        # Step 3: Form pairs using two pointers and sum their GCDs
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += get_gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum