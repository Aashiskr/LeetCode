class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(n):
            if n < 100:
                return 0
            
            s = str(n)
            memo = {}
            
            # dfs returns a tuple: (count_of_valid_numbers, sum_of_waviness)
            def dfs(idx, tight, lz, d1, d2):
                if idx == len(s):
                    return 1, 0
                
                state = (idx, tight, lz, d1, d2)
                if state in memo:
                    return memo[state]
                
                limit = int(s[idx]) if tight else 9
                total_cnt = 0
                total_wave = 0
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_lz = lz and (d == 0)
                    
                    # Update previous digits based on leading zero state
                    if new_lz:
                        new_d1 = -1
                        new_d2 = -1
                    else:
                        new_d1 = d
                        new_d2 = -1 if lz else d1
                        
                    # Check if the middle digit (d1) forms a peak or valley
                    is_wave = 0
                    if not lz and d1 != -1 and d2 != -1:
                        if d2 < d1 and d1 > d:    # Peak
                            is_wave = 1
                        elif d2 > d1 and d1 < d:  # Valley
                            is_wave = 1
                            
                    # Process the rest of the string
                    cnt, wave = dfs(idx + 1, new_tight, new_lz, new_d1, new_d2)
                    
                    total_cnt += cnt
                    total_wave += wave + is_wave * cnt
                    
                memo[state] = (total_cnt, total_wave)
                return memo[state]
            
            # Start DP: idx=0, tight=True, lz=True, d1=-1, d2=-1
            return dfs(0, True, True, -1, -1)[1]

        # Calculate range sum using prefix subtraction
        return solve(num2) - solve(num1 - 1)