class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0
        
        # We iterate through every possible starting position of a substring
        for i in range(n):
            counts = {}
            distinct_count = 0
            max_freq_in_window = 0
            
            # Expand the substring from i to the end of the string
            for j in range(i, n):
                char = s[j]
                
                # Update frequency map
                if char not in counts:
                    counts[char] = 0
                    distinct_count += 1
                counts[char] += 1
                
                # Track the frequency we need all distinct characters to match
                # (We can just use the count of the first character found at index i)
                current_length = j - i + 1
                
                # A substring is balanced ONLY if:
                # Total Length == (Number of distinct characters) * (Frequency of any one character)
                # We use counts[s[i]] as the reference frequency
                if current_length == distinct_count * counts[s[i]]:
                    # Verify all other characters match this frequency
                    is_balanced = True
                    target = counts[s[i]]
                    for char_key in counts:
                        if counts[char_key] != target:
                            is_balanced = False
                            break
                    
                    if is_balanced:
                        max_length = max(max_length, current_length)
                        
        return max_length