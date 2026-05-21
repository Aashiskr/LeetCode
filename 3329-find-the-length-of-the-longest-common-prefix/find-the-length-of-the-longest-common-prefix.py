class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        
        # Step 1: Store all possible prefixes of every number in arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Chop off the last digit
                
        max_len = 0
        
        # Step 2: Check prefixes of numbers in arr2 against the set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # Match found. Since we check the longest possible 
                    # prefix first, we can update max_len and break early.
                    max_len = max(max_len, len(str(num)))
                    break 
                num //= 10
                
        return max_len