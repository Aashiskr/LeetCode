class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # Alice can always force a win by taking either all even-indexed 
        # or all odd-indexed piles, whichever is larger.
        return True