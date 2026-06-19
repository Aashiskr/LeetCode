class Solution(object):
    def largestAltitude(self, gain):
        x = [0]
        y=0
        h=0
        for i in gain:
            y=y+i
            if y>h:
                h=y
        return h

        

            