class Solution(object):
    def countPrimeSetBits(self, left, right):
        x = 0
        for i in range(left,right+1,1):
            b=bin(i)[2:]
            c=b.count('1')
            p=0
            for j in range(1,c+1,1):
                if(c%j==0):
                    p=p+1
            if(p==2):
                x=x+1
        return x

        