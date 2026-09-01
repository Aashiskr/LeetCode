from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])
        
        litter_coords = []
        start_pos = -1
        
        # Identify coordinates for 'S' and all 'L's
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                elif classroom[r][c] == 'S':
                    start_pos = r * n + c
                    
        k = len(litter_coords)
        if k == 0:
            return 0  # No litter to clean
            
        target_mask = (1 << k) - 1
        
        litter_idx = {}
        for i, (r, c) in enumerate(litter_coords):
            litter_idx[r * n + c] = i
            
        # visited[state_idx] will store the max energy observed at that state
        # State index conceptually represents: position * (2^k) + mask
        visited = [-1] * (m * n * (1 << k))
        
        q = deque()
        # Initialize queue: (moves, position, bitmask, current_energy)
        q.append((0, start_pos, 0, energy))
        visited[start_pos * (1 << k)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            moves, pos, mask, cur_energy = q.popleft()
            
            # If we've collected all litter pieces, since it's BFS, this is our minimum moves guaranteed
            if mask == target_mask:
                return moves
                
            # If energy is 0 and we are not on the end configuration (checked right above), we are stranded
            if cur_energy == 0:
                continue
                
            r = pos // n
            c = pos % n
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    n_pos = nr * n + nc
                    cell = classroom[nr][nc]
                    
                    if cell == 'X':
                        continue
                        
                    n_mask = mask
                    if cell == 'L':
                        n_mask |= (1 << litter_idx[n_pos])
                        
                    n_energy = cur_energy - 1
                    if cell == 'R':
                        n_energy = energy
                        
                    state_idx = n_pos * (1 << k) + n_mask
                    
                    # If we reach this state with strictly more energy, explore it
                    if n_energy > visited[state_idx]:
                        visited[state_idx] = n_energy
                        q.append((moves + 1, n_pos, n_mask, n_energy))
                        
        return -1