from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        counts = Counter(s)
        
        half = []
        mid = ""
        
        # Iterate through the alphabet in order to guarantee the lexicographically smallest result
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in counts:
                count = counts[char]
                
                # If the count is odd, this character must be placed in the middle
                if count % 2 != 0:
                    mid = char
                
                # Add exactly half of the characters to our first half string
                half.append(char * (count // 2))
                
        first_half = "".join(half)
        
        # The result is the first half, the middle character (if any), and the reversed first half
        return first_half + mid + first_half[::-1]