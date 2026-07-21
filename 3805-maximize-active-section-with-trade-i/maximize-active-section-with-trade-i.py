class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: 
            return 0
        
        # Step 1: Compress string into grouped blocks of characters and lengths
        groups = []
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append((s[i-1], count))
                count = 1
        groups.append((s[-1], count))
        
        # Calculate base number of '1's if we made 0 trades
        total_ones = sum(c for char, c in groups if char == '1')
        
        # Extract purely the sizes of '0' blocks
        Z = [c for char, c in groups if char == '0']
        
        # If there are fewer than 2 blocks of '0's, no '1' block can be surrounded by '0's
        if len(Z) < 2:
            return total_ones
            
        # Keep track of the top 3 largest '0' blocks to easily look up the "Largest Other Zeros"
        top3 = sorted([(val, idx) for idx, val in enumerate(Z)], reverse=True)[:3]
        
        def get_other_max(u, v):
            """Returns the max '0' block size that is NOT at index u or v."""
            for val, idx in top3:
                if idx != u and idx != v:
                    return val
            return 0
            
        max_gain = -float('inf')
        z_idx = 0  # Tracks our index within the Z array
        
        # Step 2: Iterate through groups and test flipping each valid inner '1' block
        for i in range(len(groups)):
            if groups[i][0] == '0':
                z_idx += 1
            elif groups[i][0] == '1':
                # An inner '1' block is surrounded by '0's, hence it's not the first or last group
                if i > 0 and i < len(groups) - 1:
                    left_z = z_idx - 1
                    right_z = z_idx
                    o_size = groups[i][1]
                    
                    # Size of the new zero block if we turn this '1' block to '0's
                    merged_size = Z[left_z] + o_size + Z[right_z]
                    
                    # Size of the largest zero block elsewhere in the string
                    other_max = get_other_max(left_z, right_z)
                    
                    # We flip the most profitable zero block to 1s
                    best_flip = max(merged_size, other_max)
                    
                    # Gain = (1s we create) - (1s we destroyed)
                    gain = best_flip - o_size
                    if gain > max_gain:
                        max_gain = gain
                        
        # If no valid trades were possible (e.g. no inner 1s)
        if max_gain == -float('inf'):
            return total_ones
            
        return total_ones + max_gain