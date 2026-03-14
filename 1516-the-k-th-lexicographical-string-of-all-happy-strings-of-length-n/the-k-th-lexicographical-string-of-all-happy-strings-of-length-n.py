class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.result = ""
        self.count = 0
        
        def backtrack(current_string):
            # If we've reached the target k-th string, stop
            if self.count == k:
                return
            
            # Base case: if the string length matches n
            if len(current_string) == n:
                self.count += 1
                if self.count == k:
                    self.result = current_string
                return
            
            # Try adding 'a', 'b', and 'c' in lexicographical order
            for char in ['a', 'b', 'c']:
                # Ensure adjacent characters are not the same
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
        
        backtrack("")
        return self.result