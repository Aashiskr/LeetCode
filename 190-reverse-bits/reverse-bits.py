class Solution(object):
    def reverseBits(self, n):
        x = format(n, '032b')
        s = x[::-1]
        return int(s, 2)