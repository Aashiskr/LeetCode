class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Rule 0: Base Case - Agar n=1 hai, toh string sirf "0" hai
        if n == 1:
            return "0"
        
        # S_n ki total length nikalte hain. Formula: (2^n) - 1
        # (1 << n) ka matlab 2^n hi hota hai, ye thoda fast tarikah hai
        length = (1 << n) - 1 
        
        # String ka bilkul center (mid) point nikalte hain
        mid = (length // 2) + 1
        
        # Rule 1: Agar k bilkul beech mein hai
        if k == mid:
            return "1"
            
        # Rule 2: Agar k left side mein hai (beech se chhota)
        elif k < mid:
            return self.findKthBit(n - 1, k)
            
        # Rule 3: Agar k right side mein hai (beech se bada)
        else:
            # Piche se same position nikalte hain: (total length - k + 1)
            # Aur fir call karte hain n-1 ke liye
            corresponding_bit = self.findKthBit(n - 1, length - k + 1)
            
            # Jo bhi answer aayega, usko 'invert' (palat) kar return karna hai
            return "1" if corresponding_bit == "0" else "0"