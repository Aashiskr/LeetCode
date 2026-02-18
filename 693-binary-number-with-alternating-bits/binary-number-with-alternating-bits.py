class Solution(object):
    def hasAlternatingBits(self, n):
        x = "{0:b}".format(n)
        l = len(x)
        a = 0
        for i in range(l):
            if i%2==0 and x[i]!='1':
                a = a+1
                return False
            if i%2==1 and x[i]!='0':
                a = a+1
                return False
        if a == 0:
            return True
            
        