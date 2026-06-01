class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Based on constraints, max x is 50000.
        # We use 50005 to be safe and 1-index our coordinates.
        M = 50005 
        bit = [0] * M
        tree = [0] * (2 * M)

        # --- Fenwick Tree (BIT) Functions ---
        def add_bit(i, v):
            while i < M:
                bit[i] += v
                i += i & -i

        def query_bit(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def get_kth(k):
            """Finds the 1-based index of the k-th obstacle using binary lifting."""
            idx = 0
            # 2^16 = 65536, which is > 50005, safely covers our range.
            for i in range(16, -1, -1):
                next_idx = idx + (1 << i)
                if next_idx < M and bit[next_idx] < k:
                    idx = next_idx
                    k -= bit[next_idx]
            return idx + 1

        # --- Iterative Segment Tree Functions ---
        def update_seg(i, val):
            """Point update: set tree[i] to val and update parents."""
            i += M
            tree[i] = val
            i //= 2
            while i > 0:
                tree[i] = tree[2 * i] if tree[2 * i] > tree[2 * i + 1] else tree[2 * i + 1]
                i //= 2

        def query_seg(l, r):
            """Range maximum query in inclusive range [l, r]."""
            l += M
            r += M + 1
            res = 0
            while l < r:
                if l % 2 == 1:
                    if tree[l] > res: res = tree[l]
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    if tree[r] > res: res = tree[r]
                l //= 2
                r //= 2
            return res

        # --- Initialization ---
        # The problem states the line starts at 0. We treat 0 as a permanent obstacle.
        # Shift all coordinates by +1 so 0 maps to index 1 (BITs require 1-based indexing).
        add_bit(1, 1) 
        total_obs = 1
        results = []

        # --- Processing Queries ---
        for q in queries:
            if q[0] == 1:
                x = q[1]
                X = x + 1  # Shift coordinate
                
                # Find the number of obstacles up to X
                k = query_bit(X)
                
                # Find the obstacle immediately to the left (L)
                L_idx = get_kth(k)
                L = L_idx - 1
                
                # The gap ending at the new obstacle is x - L
                update_seg(X, x - L)
                
                # If there's an obstacle to the right (R), its gap size shrinks
                if k < total_obs:
                    R_idx = get_kth(k + 1)
                    R = R_idx - 1
                    update_seg(R_idx, R - x)
                
                # Add the new obstacle to the BIT
                add_bit(X, 1)
                total_obs += 1
                
            else:
                x, sz = q[1], q[2]
                X = x + 1
                
                k = query_bit(X)
                L_idx = get_kth(k)
                L = L_idx - 1
                
                # The largest gap is either fully contained between two obstacles <= x,
                # or it's the trailing space between the last obstacle L and x.
                max_gap = query_seg(1, L_idx)
                if x - L > max_gap:
                    max_gap = x - L
                    
                results.append(max_gap >= sz)

        return results