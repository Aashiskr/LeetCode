class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left, right = 0, n - 1
        
        # Scenario 1: Maximize distance from the first house (index 0)
        # Scan from the right end towards the left
        while colors[0] == colors[right]:
            right -= 1
        res1 = right # Distance is right - 0
        
        # Scenario 2: Maximize distance from the last house (index n-1)
        # Scan from the left end towards the right
        while colors[n - 1] == colors[left]:
            left += 1
        res2 = (n - 1) - left
        
        return max(res1, res2)