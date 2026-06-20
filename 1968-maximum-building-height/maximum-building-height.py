class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # Append the implicit restriction for the first building
        restrictions.append([1, 0])
        
        # Append a dummy restriction for the last building to bound the right side
        # A building's height can never naturally exceed its distance from building 1
        restrictions.append([n, n - 1])
        
        # Sort restrictions by building ID
        restrictions.sort()
        
        m = len(restrictions)
        
        # Pass 1: Left to Right
        # Update each restriction based on the restricted building to its left
        for i in range(1, m):
            prev_id, prev_h = restrictions[i-1]
            curr_id, curr_h = restrictions[i]
            restrictions[i][1] = min(curr_h, prev_h + (curr_id - prev_id))
            
        # Pass 2: Right to Left
        # Update each restriction based on the restricted building to its right
        for i in range(m - 2, -1, -1):
            next_id, next_h = restrictions[i+1]
            curr_id, curr_h = restrictions[i]
            restrictions[i][1] = min(curr_h, next_h + (next_id - curr_id))
            
        max_height = 0
        
        # Calculate the maximum possible peak height between each pair of adjacent restrictions
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height