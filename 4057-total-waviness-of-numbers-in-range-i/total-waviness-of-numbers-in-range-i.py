class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Numbers with fewer than 3 digits cannot have peaks or valleys
            if n < 3:
                continue
                
            # Check for peaks and valleys (excluding first and last digits)
            for i in range(1, n - 1):
                prev_digit = s[i - 1]
                curr_digit = s[i]
                next_digit = s[i + 1]
                
                # Check Peak: strictly greater than both neighbors
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # Check Valley: strictly less than both neighbors
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness