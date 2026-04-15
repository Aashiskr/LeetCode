from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        shortest_dist = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                # Calculate direct distance and wrap-around distance
                direct_dist = abs(i - startIndex)
                wrap_dist = n - direct_dist
                
                # Find the minimum of the two paths for this specific match
                current_min = min(direct_dist, wrap_dist)
                
                # Update the overall shortest distance
                shortest_dist = min(shortest_dist, current_min)
                
        # If shortest_dist is still infinity, the target was not found
        return shortest_dist if shortest_dist != float('inf') else -1