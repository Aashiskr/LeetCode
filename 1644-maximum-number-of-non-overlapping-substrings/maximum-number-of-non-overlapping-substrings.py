class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        intervals = []
        
        # For each character present, find the valid interval starting at first[c]
        for c in first:
            start = first[c]
            end = last[c]
            valid = True
            j = start
            while j <= end:
                char_j = s[j]
                if first[char_j] < start:
                    valid = False
                    break
                end = max(end, last[char_j])
                j += 1
            if valid:
                intervals.append((start, end))
        
        # Sort intervals by end time ascending, then start time ascending
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        res = []
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                res.append(s[start:end+1])
                last_end = end
        
        return res