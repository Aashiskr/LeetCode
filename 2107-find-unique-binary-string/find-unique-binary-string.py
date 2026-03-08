class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n=nums[0]
        l=len(n)
        binary_list = [''.join(i) for i in itertools.product('01', repeat=l)]
        for i in binary_list:
            if i not in nums:
                return i
        