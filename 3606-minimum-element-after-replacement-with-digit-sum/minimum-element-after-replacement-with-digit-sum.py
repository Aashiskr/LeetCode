class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate the sum of digits for each number and return the minimum of those sums
        return min(sum(int(digit) for digit in str(num)) for num in nums)