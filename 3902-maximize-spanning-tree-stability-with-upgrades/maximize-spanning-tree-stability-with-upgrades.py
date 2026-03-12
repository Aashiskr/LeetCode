class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Helper class for Disjoint Set Union (Union-Find)
        class DSU:
            def __init__(self, n, parent=None, rank=None, components=None):
                if parent is None:
                    self.parent = list(range(n))
                    self.rank = [1] * n
                    self.components = n
                else:
                    # Allow cloning of an existing DSU state
                    self.parent = list(parent)
                    self.rank = list(rank)
                    self.components = components

            def find(self, i):
                # Path compression
                while i != self.parent[i]:
                    self.parent[i] = self.parent[self.parent[i]]
                    i = self.parent[i]
                return i

            def union(self, i, j):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    # Union by rank
                    if self.rank[root_i] < self.rank[root_j]:
                        root_i, root_j = root_j, root_i
                    self.parent[root_j] = root_i
                    self.rank[root_i] += self.rank[root_j]
                    self.components -= 1
                    return True
                return False

        # 1. Global Connectivity Check
        dsu_global = DSU(n)
        for u, v, s, must in edges:
            dsu_global.union(u, v)
        if dsu_global.components > 1:
            return -1

        # 2. Mandatory edges check
        dsu_must = DSU(n)
        must_edges = []
        optional_edges = []
        min_must_s = float('inf')
        
        for u, v, s, must in edges:
            if must == 1:
                must_edges.append((u, v, s))
                min_must_s = min(min_must_s, s)
                # If mandatory edges form a cycle, it's impossible to make a valid tree
                if not dsu_must.union(u, v):
                    return -1 
            else:
                optional_edges.append((u, v, s))

        # 3. Define the Binary Search limits
        low = 1
        high = 0
        for u, v, s in must_edges:
            high = max(high, s)
        for u, v, s in optional_edges:
            high = max(high, s * 2)
            
        # Stability is capped by the weakest mandatory edge
        if min_must_s != float('inf'):
            high = min(high, min_must_s)
            
        ans = -1
        
        # 4. Binary Search
        while low <= high:
            mid = (low + high) // 2
            
            # Start with the DSU state already containing the mandatory edges
            dsu = DSU(n, dsu_must.parent, dsu_must.rank, dsu_must.components)
            
            E0 = [] # Optional edges requiring 0 upgrades
            E1 = [] # Optional edges requiring 1 upgrade
            
            for u, v, s in optional_edges:
                if s >= mid:
                    E0.append((u, v))
                elif s * 2 >= mid:
                    E1.append((u, v))
                    
            # Greedily connect 0-cost edges first
            for u, v in E0:
                dsu.union(u, v)
                
            # Then connect 1-cost edges, keeping track of upgrades
            cost = 0
            for u, v in E1:
                if dsu.union(u, v):
                    cost += 1
                    
            # Check if a spanning tree was successfully formed within the upgrade budget
            if dsu.components == 1 and cost <= k:
                ans = mid
                low = mid + 1  # We can try to achieve a higher stability
            else:
                high = mid - 1 # Stability was too high
                
        return ans