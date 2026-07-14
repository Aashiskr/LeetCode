class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sample = "123456789"
        result = []
        
        # The length of the sequential numbers can range from 2 to 9 digits
        for length in range(2, 10):
            # Iterate through possible starting positions in "123456789"
            for i in range(10 - length):
                # Slice the string to get the sequential digits and convert to int
                num = int(sample[i: i + length])
                
                # Check if it falls within the given range
                if low <= num <= high:
                    result.append(num)
                    
        return result