class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start point ascending, then by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        valid_intervals_count = 0
        max_end = -1
        
        for start, end in intervals:
            # If the current interval extends beyond the max_end we've seen,
            # it is not covered by any previous interval.
            if end > max_end:
                valid_intervals_count += 1
                max_end = end
                
        return valid_intervals_count