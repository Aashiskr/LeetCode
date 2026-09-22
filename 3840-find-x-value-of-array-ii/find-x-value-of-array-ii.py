class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        N = len(nums)
        tree = [[1] + [0] * k for _ in range(2 * N)]
        
        def make_node(val):
            v = val % k
            node = [0] * (k + 1)
            node[0] = v
            node[v + 1] = 1
            return node

        def combine(L, R):
            P_L = L[0]
            res = [0] * (k + 1)
            res[0] = (P_L * R[0]) % k
            
            # Inherit left child's prefix counts
            for i in range(1, k + 1):
                res[i] = L[i]
                
            # Append right child's prefix counts multiplied by Left's total product
            for i in range(k):
                c = R[i + 1]
                if c:
                    res[(P_L * i) % k + 1] += c
                    
            return res

        # 1. Initialize tree leaves
        for i in range(N):
            tree[N + i] = make_node(nums[i])
            
        # 2. Build the segment tree by calculating parents
        for i in range(N - 1, 0, -1):
            tree[i] = combine(tree[2 * i], tree[2 * i + 1])
            
        ans = []
        for index, value, start, x in queries:
            # Update the exact point dynamically
            idx = index + N
            tree[idx] = make_node(value)
            idx //= 2
            while idx > 0:
                tree[idx] = combine(tree[2 * idx], tree[2 * idx + 1])
                idx //= 2
                
            # Range Query for [start, N - 1]
            l = start + N
            r = N + N
            res_l = [1] + [0] * k
            res_r = [1] + [0] * k
            
            while l < r:
                if l % 2 == 1:
                    res_l = combine(res_l, tree[l])
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    res_r = combine(tree[r], res_r)
                l //= 2
                r //= 2
                
            # Resolve accumulated left & right fragments
            final_res = combine(res_l, res_r)
            
            # The count corresponds to the frequency mapped into the final combined node
            ans.append(final_res[x + 1])
            
        return ans