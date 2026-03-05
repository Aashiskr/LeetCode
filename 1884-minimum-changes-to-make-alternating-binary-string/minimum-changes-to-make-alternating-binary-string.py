class Solution(object):
    def minOperations(self, s):
        l = len(s)
        
        num_start_0 = 0
        for i in range(l):
            if i % 2 == 0 and s[i] != '0':
                num_start_0 += 1
            if i % 2 == 1 and s[i] != '1':
                num_start_0 += 1
                
        num_start_1 = 0
        for i in range(l):
            if i % 2 == 0 and s[i] != '1':
                num_start_1 += 1
            if i % 2 == 1 and s[i] != '0':
                num_start_1 += 1
        return min(num_start_0, num_start_1)