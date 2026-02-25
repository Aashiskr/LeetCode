class Solution(object):
    def sortByBits(self, arr):
        c=[]
        for i in arr:
            count = bin(i).count('1')
            a=[count,i]
            c.append(a)
        c.sort()
        l=len(c)
        arr=[]
        for i in range(l):
            arr.append(c[i][1])
        return arr


        