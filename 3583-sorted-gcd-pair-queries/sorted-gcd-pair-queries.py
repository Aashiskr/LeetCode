import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        
        # Step 1: Count frequencies of each number in nums
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        # Step 2: Compute exact counts of pairs for each possible GCD
        gcd_count = [0] * (max_val + 1)
        
        # Iterate backwards to easily subtract the multiples' already computed valid pairs
        for i in range(max_val, 0, -1):
            
            # Find how many numbers in nums are multiples of i
            multiples_count = 0
            for j in range(i, max_val + 1, i):
                multiples_count += freq[j]
            
            # Calculate total pairs where BOTH elements are multiples of i
            pairs = multiples_count * (multiples_count - 1) // 2
            
            # Subtract pairs where the strict GCD is a multiple of i, not exactly i
            for j in range(2 * i, max_val + 1, i):
                pairs -= gcd_count[j]
                
            gcd_count[i] = pairs
            
        # Step 3: Compute the prefix sum of pair counts
        # pref[x] will store the total number of pairs with GCD <= x
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + gcd_count[i]
            
        # Step 4: Answer the queries using Binary Search
        ans = []
        for q in queries:
            # We look for the first GCD whose cumulative count is strictly greater than the query index 'q'
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans