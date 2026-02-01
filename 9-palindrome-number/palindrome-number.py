class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        if(x==0):
            return True
        if(x>0):
            y=int(str(x)[::-1])
            if(y==x):
                return True
            else:
                return False
        