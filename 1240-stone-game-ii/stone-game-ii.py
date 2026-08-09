class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        # suffix[i] = total stones from piles[i] to piles[n-1]
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # No piles remaining
            if i >= n:
                return 0

            # Current player can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                # After we take X piles, opponent gets dp(...)
                opponent = dp(i + X, max(M, X))

                # Total remaining stones - opponent's maximum
                # = maximum stones we can eventually get
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)