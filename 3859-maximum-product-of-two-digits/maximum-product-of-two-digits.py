class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        max1 = 0
        max2 = 0
        
        while n > 0:
            digit = n % 10  # Extract the last digit
            
            # If we find a new maximum, the old maximum becomes the second max
            if digit >= max1:
                max2 = max1
                max1 = digit
            # If it's not greater than max1 but is greater than max2, update max2
            elif digit > max2:
                max2 = digit
                
            n //= 10  # Remove the last digit
            
        return max1 * max2