import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Dictionary to store row numbers mapped to a bitmask of reserved seats
        row_masks = collections.defaultdict(int)
        
        for row, seat in reservedSeats:
            # Set the `seat`-th bit to 1
            row_masks[row] |= (1 << seat)
            
        # Start by assuming every row is completely empty
        max_groups = 2 * n
        
        # Bitmasks for our allowed blocks:
        # Left block (seats 2, 3, 4, 5): (1<<2) | (1<<3) | (1<<4) | (1<<5) = 60
        # Middle block (seats 4, 5, 6, 7): (1<<4) | (1<<5) | (1<<6) | (1<<7) = 240
        # Right block (seats 6, 7, 8, 9): (1<<6) | (1<<7) | (1<<8) | (1<<9) = 960
        
        for row, mask in row_masks.items():
            # Deduct the 2 groups we assumed this row could fit originally
            max_groups -= 2
            
            # Check availability using bitwise AND
            can_left = (mask & 60) == 0
            can_right = (mask & 960) == 0
            can_middle = (mask & 240) == 0
            
            # Re-add the groups that can actually fit based on reservations
            if can_left and can_right:
                max_groups += 2
            elif can_left or can_right or can_middle:
                max_groups += 1
                
        return max_groups