from bisect import bisect_right

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        if not queries:
            return []
            
        # Get sorted unique values
        V = sorted(list(set(nums)))
        m = len(V)
        
        # Map values to their index in V for O(1) lookups
        val_to_idx = {v: i for i, v in enumerate(V)}
        
        # Precompute connected components
        comp = [0] * m
        curr_comp = 0
        for i in range(1, m):
            if V[i] - V[i-1] > maxDiff:
                curr_comp += 1
            comp[i] = curr_comp
            
        # Binary lifting table: up[i][j] is the max index reachable from i in 2^j jumps
        up = [[0] * 18 for _ in range(m)]
        
        # Initialize the 0-th power (1 jump) using a two-pointer approach
        right = 0
        for i in range(m):
            while right + 1 < m and V[right + 1] <= V[i] + maxDiff:
                right += 1
            up[i][0] = right
            
        # Populate the rest of the binary lifting table
        for j in range(1, 18):
            for i in range(m):
                up[i][j] = up[ up[i][j-1] ][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            
            valU, valV = nums[u], nums[v]
            if valU == valV:
                # Different nodes but identical value => connected by 1 edge
                ans.append(1)
                continue
            
            A, B = min(valU, valV), max(valU, valV)
            idxA, idxB = val_to_idx[A], val_to_idx[B]
            
            # If they are in isolated components
            if comp[idxA] != comp[idxB]:
                ans.append(-1)
                continue
            
            # Binary lifting to find the minimum steps
            curr = idxA
            steps = 0
            for j in range(17, -1, -1):
                if up[curr][j] < idxB:
                    curr = up[curr][j]
                    steps += 1 << j
            
            ans.append(steps + 1)
            
        return ans