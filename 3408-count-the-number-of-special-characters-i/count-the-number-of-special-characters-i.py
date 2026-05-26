class Solution(object):
    def numberOfSpecialChars(self, word):
        s = 0
        counted = set() 
        
        for i in word:
            
            if i.islower() and i not in counted:
                u = i.upper()
                if u in word:
                    s = s + 1
                    counted.add(i) 
        return s