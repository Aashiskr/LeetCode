class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # last_seen_reversed maps the value 'reverse(nums[i])' to index 'i'
        # This allows us to find the closest 'i' for a future nums[j]
        last_seen_reversed = {}
        min_dist = float('inf')
        
        def get_reverse(n: int) -> int:
            res = 0
            while n > 0:
                res = res * 10 + (n % 10)
                n //= 10
            return res

        for j, val in enumerate(nums):
            # Check if current nums[j] matches any previous reverse(nums[i])
            if val in last_seen_reversed:
                dist = j - last_seen_reversed[val]
                if dist < min_dist:
                    min_dist = dist
            
            # Store the reverse of the current number to match future nums[k]
            # If nums[j] = 12, we store {21: j}
            rev_val = get_reverse(val)
            last_seen_reversed[rev_val] = j
            
        return min_dist if min_dist != float('inf') else -1