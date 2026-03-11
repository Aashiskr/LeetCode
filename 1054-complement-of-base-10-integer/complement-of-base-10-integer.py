class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Calculate the bit length of n
        # For n=5 (101), bit_length is 3
        bit_length = n.bit_length()
        
        # Create a mask of all 1s (e.g., for length 3, mask is 111)
        # (1 << 3) is 1000, then subtract 1 to get 111
        mask = (1 << bit_length) - 1
        
        # XOR n with the mask to flip the bits
        return n ^ mask