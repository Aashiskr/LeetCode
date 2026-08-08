class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        N = len(word1)
        M = len(word2)
        
        # right[j] will store the maximum index in word1 that can match word2[j] 
        # such that the suffix word2[j:] is a subsequence of word1[right[j]:]
        right = [-1] * M
        j = M - 1
        for i in range(N - 1, -1, -1):
            if word1[i] == word2[j]:
                right[j] = i
                j -= 1
                if j < 0:
                    break
        
        ans = []
        j = 0
        changed = False
        
        # Greedily build the sequence from left to right
        for i in range(N):
            if j == M:
                break
                
            if word1[i] == word2[j]:
                # Exact match
                ans.append(i)
                j += 1
            elif not changed and (j + 1 == M or right[j + 1] > i):
                # Use the allowed single character mismatch
                # Valid because the remaining characters in word2 can match exactly in the rest of word1
                ans.append(i)
                changed = True
                j += 1
                
        # If we successfully found all M indices, return them
        if len(ans) == M:
            return ans
            
        return []