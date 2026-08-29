class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        n = len(nums)

        # Store every value together with its original index.
        pairs = [(nums[i], i) for i in range(n)]

        # Sorting by value lets us identify connected swapping groups.
        pairs.sort()

        answer = nums[:]
        start = 0

        while start < n:
            end = start

            # Extend the group while neighbouring sorted values
            # differ by at most limit.
            while (
                end + 1 < n
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Values are already sorted because pairs is sorted.
            values = [pairs[i][0] for i in range(start, end + 1)]

            # Sort the original indices belonging to this group.
            indices = sorted(
                pairs[i][1] for i in range(start, end + 1)
            )

            # Smallest value goes to the smallest available index.
            for index, value in zip(indices, values):
                answer[index] = value

            start = end + 1

        return answer