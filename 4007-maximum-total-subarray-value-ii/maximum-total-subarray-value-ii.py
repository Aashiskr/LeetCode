import math
import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        # Precompute integer logarithms to answer Range Queries in O(1)
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1
            
        LOG = log_table[n] + 1
        
        # Initialize Sparse Tables for Range Maximum and Range Minimum
        max_st = [None] * LOG
        min_st = [None] * LOG
        
        max_st[0] = list(nums)
        min_st[0] = list(nums)
        
        # Build Sparse Tables 
        # Using list comprehensions for high C-level execution speed in Python
        for j in range(1, LOG):
            length = 1 << j
            half = 1 << (j - 1)
            size = n - length + 1
            
            prev_max = max_st[j - 1]
            max_st[j] = [prev_max[i] if prev_max[i] > prev_max[i + half] else prev_max[i + half] for i in range(size)]
            
            prev_min = min_st[j - 1]
            min_st[j] = [prev_min[i] if prev_min[i] < prev_min[i + half] else prev_min[i + half] for i in range(size)]
            
        # Helper method to query max - min in O(1) Time
        def get_val(L, R):
            length = R - L + 1
            j = log_table[length]
            
            arr_max = max_st[j]
            m1 = arr_max[L]
            m2 = arr_max[R - (1 << j) + 1]
            mx = m1 if m1 > m2 else m2
            
            arr_min = min_st[j]
            m3 = arr_min[L]
            m4 = arr_min[R - (1 << j) + 1]
            mn = m3 if m3 < m4 else m4
            
            return mx - mn
            
        # Initialize Max Heap (using negated values to simulate max-heap in Python)
        # We start with the largest possible subarray for each starting index `i`
        heap = []
        for i in range(n):
            v = get_val(i, n - 1)
            heap.append((-v, i, n - 1))
            
        heapq.heapify(heap)
        
        ans = 0
        
        # Pull the absolute maximum `k` times
        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans -= neg_v
            
            # The next largest potential subarray for this start index is r - 1
            if r > l:
                v_new = get_val(l, r - 1)
                heapq.heappush(heap, (-v_new, l, r - 1))
                
        return ans