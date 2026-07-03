class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()
        
        # 1. Build adjacency list with only valid edges
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                unique_costs.add(cost)
                
        # 2. Topological sort using Kahn's Algorithm
        q = [i for i in range(n) if in_degree[i] == 0]
        topo = []
        
        # Using a pointer is faster than pop(0) on a list
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            topo.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Extract unique edge costs to binary search over
        costs = sorted(list(unique_costs))
        if not costs:
            return -1
            
        # Helper function to check if a path exists with all edge costs >= X and total cost <= k
        def check(X):
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo:
                d = dist[u]
                if d != float('inf'):
                    for v, cost in adj[u]:
                        if cost >= X:  # Only consider edges meeting the minimum cost threshold
                            if d + cost < dist[v]:
                                dist[v] = d + cost
                                
            return dist[n - 1] <= k

        # 3. Binary Search over unique costs
        low = 0
        high = len(costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(costs[mid]):
                ans = costs[mid]
                low = mid + 1   # feasible, try for a higher minimum edge cost
            else:
                high = mid - 1  # not feasible, lower the minimum threshold requirement
                
        return ans