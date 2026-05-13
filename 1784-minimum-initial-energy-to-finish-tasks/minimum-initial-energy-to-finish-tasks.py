class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort tasks by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            # If we don't have enough energy to start the task, 
            # we need to increase our starting energy pool.
            if current_energy < minimum:
                shortfall = minimum - current_energy
                initial_energy += shortfall
                current_energy += shortfall
            
            # Spend the actual energy required for the task
            current_energy -= actual
            
        return initial_energy