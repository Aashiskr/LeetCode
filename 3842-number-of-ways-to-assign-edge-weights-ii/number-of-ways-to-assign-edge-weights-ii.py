import collections

class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Build Depth and Ancestor array using BFS to avoid recursion limit
        queue = collections.deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    # Calculate 2^i-th ancestor
                    for i in range(1, LOG):
                        up[v][i] = up[up[v][i - 1]][i - 1]
                    queue.append(v)
                    
        def get_lca(u, v):
            # Bring both nodes to the same depth
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
                    
            if u == v:
                return u
                
            # Ascend both nodes together
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
                    
            return up[u][0]
            
        MOD = 10**9 + 7
        
        # Precompute powers of 2 modulo 10^9 + 7
        p2 = [1] * (n + 1)
        for i in range(1, n + 1):
            p2[i] = (p2[i - 1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[lca]
            
            if L == 0:
                ans.append(0)
            else:
                ans.append(p2[L - 1])
                
        return ans