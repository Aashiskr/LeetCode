class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Sort costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the sorted candies
        for i in range(len(cost)):
            # We pay for the 1st and 2nd candies in every group of 3.
            # We skip paying for the 3rd candy (indices 2, 5, 8...).
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost