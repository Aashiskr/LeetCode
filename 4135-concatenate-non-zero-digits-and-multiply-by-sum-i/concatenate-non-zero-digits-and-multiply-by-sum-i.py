class Solution(object):
    def sumAndMultiply(self, n):
        j=0
        sum = 0
        n = str(n)
        for k in n:
            i =int(k)
            if i!=0:
                j=j*10+i
                sum=sum+i
        return sum*j
                
        