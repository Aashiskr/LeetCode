import math

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Step 1: Calculate character frequencies
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        mid_char = ""
        half_counts = {}
        for char, count in freq.items():
            if count % 2 != 0:
                mid_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        # Step 2: Compute initial total permutations (W) of the first half
        M = sum(half_counts.values())
        
        W = math.factorial(M)
        for count in half_counts.values():
            W //= math.factorial(count)
            
        # If k exceeds the total possible unique palindromic permutations
        if k > W:
            return ""
            
        # Step 3: Build the k-th permutation of the first half
        chars = sorted(half_counts.keys())
        half_str = []
        
        while M > 0:
            for c in chars:
                if half_counts[c] > 0:
                    # Calculate permutations available if we choose character `c`
                    ways = W * half_counts[c] // M
                    
                    if k <= ways:
                        # The k-th permutation falls within this branch
                        half_str.append(c)
                        W = ways
                        half_counts[c] -= 1
                        M -= 1
                        break
                    else:
                        # Skip this branch entirely
                        k -= ways
                        
        # Step 4: Construct the final palindrome string
        left_half = "".join(half_str)
        return left_half + mid_char + left_half[::-1]