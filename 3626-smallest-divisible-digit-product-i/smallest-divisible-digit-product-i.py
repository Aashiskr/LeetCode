class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        # Helper function to calculate the product of digits
        def get_digit_product(num):
            product = 1
            while num > 0:
                product *= (num % 10)
                num //= 10
            return product
        
        # Start from n and keep incrementing until the condition is met
        while True:
            if get_digit_product(n) % t == 0:
                return n
            n += 1