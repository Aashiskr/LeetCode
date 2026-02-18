class Solution(object):
    def hasAlternatingBits(self, n):
        x = "{0:b}".format(n)
        l = len(x)
        a = 0
        for i in range(l):
            if i%2==0 and x[i]!='1':
                return False
            if i%2==1 and x[i]!='0':
                return False
        return True
            
        