class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]
        l = len(b)
        x = 0
        a = 999
        c = 999
        
        for i in range(l):
            if b[i] == '1':
                if a == 999:
                    a = i
                else:
                    c = i
                    if x < c - a:
                        x = c - a
                    a = c
                    c = 999
        return x