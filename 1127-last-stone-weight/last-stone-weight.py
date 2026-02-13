class Solution(object):
    def lastStoneWeight(self, stones):
        while(len(stones)!=1):
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)
            if(m1==m2):
                stones.append(m1-m2)
            else:
                x = m1-m2
                stones.append(x)
                x = 0
                m1 = 0
                m2 = 0
        return stones[0]
            

        