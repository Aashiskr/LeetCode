class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Step 1: Reverse the digits by converting to string and slicing
        # str(n)[::-1] reverses the string representation of n
        reversed_n = int(str(n)[::-1])
        
        # Step 2: Calculate the absolute difference
        return abs(n - reversed_n)