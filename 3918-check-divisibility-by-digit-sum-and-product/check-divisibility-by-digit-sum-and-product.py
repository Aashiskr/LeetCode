class Solution(object):
    def checkDivisibility(self, n):
        s=str(n)
        sum=0
        mul=1
        fin=0
        for i in s:
            sum=sum+int(i)
            mul=mul*int(i)
        fin=sum+mul
        if(n%fin==0):
            return True
        else:
            return False
            
