class Solution:
    def concatenatedBinary(self, n: int) -> int:
        a = ""
        for i in range(1, n + 1):
            b_s = f"{i:b}" 
            a = a + b_s
            
        return int(a, 2) % (10**9 + 7)