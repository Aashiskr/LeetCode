from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # Queue stores the indices we need to visit
        queue = deque([start])
        # Set keeps track of visited indices to prevent infinite loops
        visited = set([start])
        
        while queue:
            curr = queue.popleft()
            
            # If we reach an index with value 0, we found a valid path
            if arr[curr] == 0:
                return True
            
            # Calculate the two possible next jump indices
            jump_right = curr + arr[curr]
            jump_left = curr - arr[curr]
            
            # Check if jumping right is within bounds and not yet visited
            if jump_right < len(arr) and jump_right not in visited:
                visited.add(jump_right)
                queue.append(jump_right)
                
            # Check if jumping left is within bounds and not yet visited
            if jump_left >= 0 and jump_left not in visited:
                visited.add(jump_left)
                queue.append(jump_left)
                
        # If the queue empties and we haven't found a 0, it's unreachable
        return False