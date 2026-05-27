class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        last_lower = {}
        first_upper = {}
        
        # Record the relevant indices for each character
        for i, char in enumerate(word):
            if char.islower():
                # Constantly update to get the LAST occurrence
                last_lower[char] = i
            else:
                # Only record if it's not in the dictionary to get the FIRST occurrence
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        # Check all lowercase letters we found
        for char, last_idx in last_lower.items():
            upper_char = char.upper()
            
            # If the uppercase version exists AND the last lowercase index is 
            # strictly before the first uppercase index
            if upper_char in first_upper and last_idx < first_upper[upper_char]:
                special_count += 1
                
        return special_count