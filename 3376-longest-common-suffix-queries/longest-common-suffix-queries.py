class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()
        
        # 1. Determine the default best index for the empty suffix 
        # (This handles cases where the longest common suffix is "")
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
                
        root.best_idx = global_best_idx
        
        # 2. Build the Trie using reversed words
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                # Update the best index at this node
                # We only overwrite if the new string is strictly shorter.
                # If lengths are equal, we do nothing because the existing 
                # index is guaranteed to be smaller (since we iterate sequentially).
                if curr.best_idx == -1 or len(word) < len(wordsContainer[curr.best_idx]):
                    curr.best_idx = i
                        
        # 3. Process each query
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_idx)
            
        return ans