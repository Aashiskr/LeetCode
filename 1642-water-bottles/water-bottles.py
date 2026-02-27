class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        res = numBottles
        while(numExchange<=numBottles):
            r = numBottles%numExchange
            numBottles = numBottles//numExchange
            res=res+numBottles
            numBottles=numBottles+r
        return res