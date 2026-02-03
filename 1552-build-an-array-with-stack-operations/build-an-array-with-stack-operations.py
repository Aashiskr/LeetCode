class Solution(object):
    def buildArray(self, target, n):
        x = []
        l = target[-1]
        for i in range(1,n+1,1):
            if i in target:
                x.append("Push")
            if i not in target:
                x.append("Push")
                x.append("Pop")
            if(i == l):
                break
        return x
        