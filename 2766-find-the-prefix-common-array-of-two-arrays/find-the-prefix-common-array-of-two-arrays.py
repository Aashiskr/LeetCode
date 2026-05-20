class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        # Array to store the frequency of each number seen so far
        # Size is n + 1 because the numbers range from 1 to n
        seen_counts = [0] * (n + 1)
        
        common_count = 0
        C = []
        
        for i in range(n):
            # Process the number from array A
            seen_counts[A[i]] += 1
            if seen_counts[A[i]] == 2:
                common_count += 1
                
            # Process the number from array B
            seen_counts[B[i]] += 1
            if seen_counts[B[i]] == 2:
                common_count += 1
                
            # Record the number of common elements at this prefix
            C.append(common_count)
            
        return C