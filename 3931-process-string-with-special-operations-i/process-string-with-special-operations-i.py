class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        
        for char in s:
            if char == '*':
                # Remove the last character if the string is not empty
                # Python slicing handles empty strings safely (e.g., ""[:-1] remains "")
                result = result[:-1]
            elif char == '#':
                # Duplicate the current result
                result = result + result
            elif char == '%':
                # Reverse the current result
                result = result[::-1]
            else:
                # Append the lowercase English letter
                result += char
                
        return result