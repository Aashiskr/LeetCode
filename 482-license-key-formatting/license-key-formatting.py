class Solution(object):
    def licenseKeyFormatting(self, s, k):
        # List banao bina dashes ke (Uppercase mein)
        x = []
        for i in s:
            if i != "-":
                x.append(i.upper())
        
        count = 0
        # Peeche se loop chalao
        # range(len(x)-1, -1, -1) ka matlab: last index se 0 tak
        for i in range(len(x)-1, -1, -1):
            count = count + 1
            
            # Agar k characters ho gaye aur ye start (0) nahi hai
            if count == k and i != 0: # i != 0 zaroori hai taki start me dash na aaye
                x.insert(i, "-") # Wahi insert karo
                count = 0 # IMPORTANT: Count wapas 0 karo!
                
        return "".join(x)