class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        
        # Iterate through all possible valid hours (0 to 11)
        for h in range(12):
            # Iterate through all possible valid minutes (0 to 59)
            for m in range(60):
                # Count the number of set bits (1s) in binary representations of h and m
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format the time as H:MM
                    # :02d ensures the minute is zero-padded to 2 digits
                    result.append("{}:{:02d}".format(h, m))
                    
        return result