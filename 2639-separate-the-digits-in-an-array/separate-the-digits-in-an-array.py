class Solution(object):
    def separateDigits(self, nums):
        x = []
        for i in nums:
            for digit in str(i):
                x.append(int(digit))
        return x