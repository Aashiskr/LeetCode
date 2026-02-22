class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]
        l = len(b)
        x = 0
        a = 999
        c = 999
        
        for i in range(l):
            if b[i] == '1':
                # Agar pehla '1' mila hai
                if a == 999:
                    a = i
                # Agar agla '1' mila hai
                else:
                    c = i
                    
                    # Distance check karo aur max update karo
                    if x < c - a:
                        x = c - a
                    
                    # MOST IMPORTANT FIX: 
                    # Agli calculation ke liye 'a' ko hamesha naye '1' (yani c) par set karo
                    a = c
                    c = 999
                    
        return x