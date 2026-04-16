from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Group indices by their values
        val_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            val_to_indices[val].append(idx)
        
        # Dictionary to store the pre-calculated min distance for each index
        min_dist_at_index = {}
        
        for val, idxs in val_to_indices.items():
            k = len(idxs)
            if k <= 1:
                # No other index has this value
                for idx in idxs:
                    min_dist_at_index[idx] = -1
                continue
            
            # For each index in the sorted list idxs
            for i in range(k):
                curr_idx = idxs[i]
                
                # Check neighbor to the left (circular)
                left_idx = idxs[(i - 1) % k]
                dist_left = abs(curr_idx - left_idx)
                dist_left = min(dist_left, n - dist_left)
                
                # Check neighbor to the right (circular)
                right_idx = idxs[(i + 1) % k]
                dist_right = abs(curr_idx - right_idx)
                dist_right = min(dist_right, n - dist_right)
                
                min_dist_at_index[curr_idx] = min(dist_left, dist_right)
        
        # Build the answer based on queries
        return [min_dist_at_index[q] for q in queries]