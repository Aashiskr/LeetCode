class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        initial_ones = s.count('1')
        
        # 1. Identify all maximal contiguous zero groups
        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zero_groups.append({'start': start, 'length': i - start, 'end': i - 1})
            else:
                i += 1
        
        m = len(zero_groups)
        
        # 2. Map indices to zero groups for O(1) lookups
        group_idx = [-1] * n
        for idx, g in enumerate(zero_groups):
            for k in range(g['start'], g['end'] + 1):
                group_idx[k] = idx
                
        # next_group[k] is the smallest group index i such that zero_groups[i]['end'] >= k
        next_group = [m] * n
        g_ptr = 0
        for k in range(n):
            while g_ptr < m and zero_groups[g_ptr]['end'] < k:
                g_ptr += 1
            if g_ptr < m:
                next_group[k] = g_ptr
                
        # prev_group[k] is the largest group index i such that zero_groups[i]['start'] <= k
        prev_group = [-1] * n
        g_ptr = -1
        for k in range(n):
            while g_ptr + 1 < m and zero_groups[g_ptr + 1]['start'] <= k:
                g_ptr += 1
            prev_group[k] = g_ptr
            
        # 3. Build a Sparse Table for Category 3 queries (fully contained adjacent pairs)
        if m > 1:
            W = [zero_groups[idx]['length'] + zero_groups[idx+1]['length'] for idx in range(m - 1)]
            k_len = len(W)
            max_log = k_len.bit_length()
            st = [[0] * k_len for _ in range(max_log)]
            for idx in range(k_len):
                st[0][idx] = W[idx]
            for j in range(1, max_log):
                length = 1 << (j - 1)
                for idx in range(k_len - (1 << j) + 1):
                    st[j][idx] = max(st[j-1][idx], st[j-1][idx + length])
                    
            def query_max(L, R):
                if L > R:
                    return 0
                j = (R - L + 1).bit_length() - 1
                return max(st[j][L], st[j][R - (1 << j) + 1])
        else:
            def query_max(L, R):
                return 0
                
        # 4. Process each query in O(1) time
        ans = []
        for l, r in queries:
            a = group_idx[l] if s[l] == '0' else next_group[l]
            b = group_idx[r] if s[r] == '0' else prev_group[r]
                
            if a == m or b == -1 or a >= b:
                ans.append(initial_ones)
                continue
                
            max_gain = 0
            
            # Category 1: Pair starting at index a (i = a)
            left_gain = (zero_groups[a]['end'] - l + 1) if s[l] == '0' else zero_groups[a]['length']
            if a + 1 == b and s[r] == '0':
                right_gain = r - zero_groups[b]['start'] + 1
            else:
                right_gain = zero_groups[a+1]['length']
            max_gain = max(max_gain, left_gain + right_gain)
            
            # Category 2: Pair ending at index b (i = b - 1)
            if b - 1 > a:
                left_gain = zero_groups[b-1]['length']
                right_gain = (r - zero_groups[b]['start'] + 1) if s[r] == '0' else zero_groups[b]['length']
                max_gain = max(max_gain, left_gain + right_gain)
                
            # Category 3: Pairs strictly between a and b (i in [a + 1, b - 2])
            if a + 1 <= b - 2:
                max_gain = max(max_gain, query_max(a + 1, b - 2))
                
            ans.append(initial_ones + max_gain)
            
        return ans