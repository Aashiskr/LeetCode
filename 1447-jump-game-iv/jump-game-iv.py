from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        # Base case: If the array has 1 or 0 elements, we are already at the end
        if n <= 1:
            return 0
            
        # Step 1: Group indices by their values to quickly find "teleport" locations
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # Step 2: Initialize BFS
        # queue stores tuples of (current_index, current_step_count)
        queue = deque([(0, 0)]) 
        visited = {0} # Set to keep track of visited indices
        
        # Step 3: Traverse the graph
        while queue:
            curr_index, steps = queue.popleft()
            
            # If we've reached the last index, return the step count
            if curr_index == n - 1:
                return steps
                
            # Collect all possible next jumps
            next_jumps = []
            
            # 1. Jump to same values (teleportation)
            if arr[curr_index] in graph:
                next_jumps.extend(graph[arr[curr_index]])
                # CRITICAL: Clear this list from the dictionary to prevent redundant O(N) looping
                del graph[arr[curr_index]]
                
            # 2. Jump forward
            if curr_index + 1 < n:
                next_jumps.append(curr_index + 1)
                
            # 3. Jump backward
            if curr_index - 1 >= 0:
                next_jumps.append(curr_index - 1)
                
            # Add unvisited jumps to the queue
            for next_idx in next_jumps:
                if next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
        return -1