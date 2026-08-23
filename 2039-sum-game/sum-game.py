class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        
        s1 = s2 = 0
        q1 = q2 = 0
        
        # Tally sums and question marks for the left half
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])
                
        # Tally sums and question marks for the right half
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])
                
        # If total '?' is odd, Alice gets the last move and guarantees a win
        if (q1 + q2) % 2 != 0:
            return True
            
        # Bob wins if he can perfectly balance the sums using the 9-pairing strategy
        # Return True (Alice wins) if Bob's winning condition is NOT met
        return 2 * (s1 - s2) != 9 * (q2 - q1)