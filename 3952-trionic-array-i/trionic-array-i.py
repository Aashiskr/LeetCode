class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # Constraints ke mutabiq n kam se kam 3 hona chahiye
        if n < 3:
            return False
            
        i = 0
        
        # Phase 1: Strictly Increasing (Upward trend to Peak 'p')
        # Humein i + 1 < n check karna hai taaki index out of bounds na ho
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        p = i
        # Peak shuru mein nahi ho sakti (0 < p) aur na hi array ke end par
        if p == 0 or p == n - 1:
            return False
            
        # Phase 2: Strictly Decreasing (Downward trend to Valley 'q')
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            
        q = i
        # Valley peak ke turant baad honi chahiye (p < q) 
        # aur q ko array ke end se pehle hona chahiye (q < n - 1)
        if q == p or q == n - 1:
            return False
            
        # Phase 3: Second Strictly Increasing (Upward trend to the end)
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # Agar humne teeno trends follow karke array ke aakhir tak (n-1) pahunch gaye,
        # toh iska matlab array Trionic hai.
        return i == n - 1