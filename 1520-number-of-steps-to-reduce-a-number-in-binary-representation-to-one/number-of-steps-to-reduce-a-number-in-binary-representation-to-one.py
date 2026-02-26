class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = int(s, 2)
        x = 0
        while(num!=1):
            if num%2==0:
                num=num//2
                x = x+1
            else:
                num = num+1
                x = x+1
        return x


        