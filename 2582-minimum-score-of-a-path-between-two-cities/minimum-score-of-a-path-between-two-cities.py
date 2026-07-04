from collections import defaultdict, deque

class Solution(object):
    def minScore(self, n, roads):
        # 1. Build an adjacency list for the graph
        adj = defaultdict(list)
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))
            
        # 2. Initialize BFS from city 1
        queue = deque([1])
        visited = set([1])
        min_score = float('inf')
        
        # 3. Traverse the connected component
        while queue:
            node = queue.popleft()
            
            for neighbor, distance in adj[node]:
                # Update the minimum score found so far in this component
                min_score = min(min_score, distance)
                
                # If we haven't visited this neighbor, add it to the queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score