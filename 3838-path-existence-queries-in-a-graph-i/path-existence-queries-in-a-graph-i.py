class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Array to store the connected component ID for each node
        component_id = [0] * n
        current_id = 0
        
        # Precompute the connected components
        for i in range(1, n):
            # If the gap is too large, we break into a new component
            if nums[i] - nums[i - 1] > maxDiff:
                current_id += 1
            component_id[i] = current_id
            
        # Answer all queries in O(1) time each
        result = []
        for u, v in queries:
            result.append(component_id[u] == component_id[v])
            
        return result