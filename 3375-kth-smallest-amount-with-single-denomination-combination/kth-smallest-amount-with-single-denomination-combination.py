class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        # Custom Euclidean GCD to ensure compatibility with all Python environments
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Step 1: Optimize by removing redundant coins
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
                
        # Step 2: Precompute LCMs for all non-empty subsets (Principle of Inclusion-Exclusion)
        pie_data = []
        n = len(filtered_coins)
        
        for mask in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            
            for i in range(n):
                if mask & (1 << i):
                    current_lcm = (current_lcm * filtered_coins[i]) // gcd(current_lcm, filtered_coins[i])
                    set_bits += 1
            
            sign = 1 if set_bits % 2 == 1 else -1
            pie_data.append((current_lcm, sign))
            
        def count_amounts_up_to(x):
            count = 0
            for lcm_val, sign in pie_data:
                count += sign * (x // lcm_val)
            return count

        # Step 3: Binary Search for the k-th smallest amount
        left = 1
        right = filtered_coins[0] * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if count_amounts_up_to(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans