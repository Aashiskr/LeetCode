class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # 1. Factorize t for prime factors 2, 3, 5, 7
        temp = t
        t2 = t3 = t5 = t7 = 0
        while temp % 2 == 0: t2 += 1; temp //= 2
        while temp % 3 == 0: t3 += 1; temp //= 3
        while temp % 5 == 0: t5 += 1; temp //= 5
        while temp % 7 == 0: t7 += 1; temp //= 7
        
        # If t has any prime factors > 7, no combination of digits (1-9) can satisfy it
        if temp > 1: return "-1"
        
        def get_factors(d):
            if d == 1: return 0, 0, 0, 0
            if d == 2: return 1, 0, 0, 0
            if d == 3: return 0, 1, 0, 0
            if d == 4: return 2, 0, 0, 0
            if d == 5: return 0, 0, 1, 0
            if d == 6: return 1, 1, 0, 0
            if d == 7: return 0, 0, 0, 1
            if d == 8: return 3, 0, 0, 0
            if d == 9: return 0, 2, 0, 0
            return 0, 0, 0, 0
            
        memo = {}
        def min_len_23(c2, c3):
            """DP to find minimum number of digits needed to fulfill the remaining 2s and 3s factors"""
            c2, c3 = max(0, c2), max(0, c3)
            if c2 == 0 and c3 == 0: 
                return 0
            
            if (c2, c3) in memo: 
                return memo[(c2, c3)]
            
            res = float('inf')
            
            # Map of (provided_2s, provided_3s) for digits 8, 9, 6, 4, 3, 2
            digit_factor_gains = [(3, 0), (0, 2), (1, 1), (2, 0), (0, 1), (1, 0)]
            
            for d2, d3 in digit_factor_gains:
                nc2, nc3 = max(0, c2 - d2), max(0, c3 - d3)
                # Only proceed if the state strictly progresses (prevents infinite recursion)
                if (nc2, nc3) != (c2, c3):
                    res = min(res, 1 + min_len_23(nc2, nc3))
                    
            memo[(c2, c3)] = res
            return res

        def get_min_len(c2, c3, c5, c7):
            # 5s and 7s inherently require exactly 1 digit ('5' and '7') per needed factor
            return max(0, c5) + max(0, c7) + min_len_23(c2, c3)

        # 2. Check if the initial `num` is already zero-free and completely valid
        if '0' not in num:
            p2 = p3 = p5 = p7 = 0
            for char in num:
                d2, d3, d5, d7 = get_factors(int(char))
                p2 += d2; p3 += d3; p5 += d5; p7 += d7
            if p2 >= t2 and p3 >= t3 and p5 >= t5 and p7 >= t7:
                return num
                
        # 3. Precompute prefix factors to query in O(1) inside loop
        pref_factors = []
        p2 = p3 = p5 = p7 = 0
        z_idx = len(num)
        
        for i, char in enumerate(num):
            pref_factors.append((p2, p3, p5, p7))
            d = int(char)
            if d == 0:
                if z_idx == len(num): 
                    z_idx = i
            else:
                d2, d3, d5, d7 = get_factors(d)
                p2 += d2; p3 += d3; p5 += d5; p7 += d7
                
        # 4. Helper to greedily construct the rest of the string suffix
        def build_greedy(prefix, target_length, r2, r3, r5, r7):
            res = list(prefix)
            rem_len = target_length - len(prefix)
            
            for _ in range(rem_len):
                rem_len -= 1
                for v in range(1, 10):
                    d2, d3, d5, d7 = get_factors(v)
                    nr2, nr3 = max(0, r2 - d2), max(0, r3 - d3)
                    nr5, nr7 = max(0, r5 - d5), max(0, r7 - d7)
                    if get_min_len(nr2, nr3, nr5, nr7) <= rem_len:
                        res.append(str(v))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)
            
        # 5. Look for the best diverging factor looping downwards for smallest magnitude divergence
        for i in range(min(len(num) - 1, z_idx), -1, -1):
            p2, p3, p5, p7 = pref_factors[i]
            r2, r3 = max(0, t2 - p2), max(0, t3 - p3)
            r5, r7 = max(0, t5 - p5), max(0, t7 - p7)
            
            for d in range(int(num[i]) + 1, 10):
                d2, d3, d5, d7 = get_factors(d)
                nr2, nr3 = max(0, r2 - d2), max(0, r3 - d3)
                nr5, nr7 = max(0, r5 - d5), max(0, r7 - d7)
                
                rem_len = len(num) - 1 - i
                if get_min_len(nr2, nr3, nr5, nr7) <= rem_len:
                    return build_greedy(num[:i] + str(d), len(num), nr2, nr3, nr5, nr7)
                    
        # 6. Fallback step if we simply cannot manipulate 'num' at its current length
        req_len = get_min_len(t2, t3, t5, t7)
        target_length = max(len(num) + 1, req_len)
        return build_greedy("", target_length, t2, t3, t5, t7)