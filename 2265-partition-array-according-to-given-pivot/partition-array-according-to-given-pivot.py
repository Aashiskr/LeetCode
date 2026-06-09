class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less_than = []
        equal_to = []
        greater_than = []
        
        # Distribute elements into their respective buckets
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)
                
        # Concatenate the lists to form the final partitioned array
        return less_than + equal_to + greater_than