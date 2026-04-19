class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        max_dist = 0
        n, m = len(nums1), len(nums2)
        
        while i < n and j < m:
            # If the condition is met, calculate distance and try to find a larger distance by moving j
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            # If nums1[i] is too large, moving j further will only give smaller numbers. 
            # We need a smaller number from nums1, so we move i.
            else:
                i += 1
                
        return max_dist