class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        lookup = {}
        for i, num in enumerate(sorted_nums):
            if num not in lookup:
                lookup[num] = i
        return [lookup[x] for x in nums]