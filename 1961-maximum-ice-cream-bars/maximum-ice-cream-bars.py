class Solution(object):
    def maxIceCream(self, costs, coins):
        x=0
        costs.sort()
        for i in costs:
            if coins>=i:
                coins=coins-i
                x=x+1
        return x

        