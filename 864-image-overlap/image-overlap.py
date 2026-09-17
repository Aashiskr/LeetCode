from collections import Counter

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        # Collect coordinates of all 1s in both images
        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not list1 or not list2:
            return 0
        
        # Count frequency of each translation vector
        shifts = Counter()
        for r1, c1 in list1:
            for r2, c2 in list2:
                shifts[(r2 - r1, c2 - c1)] += 1
                
        return max(shifts.values())