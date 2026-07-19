class Solution(object):
    def smallestSubsequence(self, s):
        # 1. Record the last index of every character in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set() # To keep track of what's currently in our stack
        
        for i, char in enumerate(s):
            # If we've already placed this character in our ideal spot, skip it
            if char in seen:
                continue
                
            # If the current character is smaller than the last one in the stack
            # AND the last character in the stack shows up again later in the string
            # We pop it off the stack so we can put the smaller character first
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        # Join the list of characters back into a string
        return "".join(stack)