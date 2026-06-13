class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        
        for word in words:
            # 1. Calculate the total weight of the word
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # 2. Take the modulo 26
            mod_val = word_weight % 26
            
            # 3. Map to reverse alphabetical order (0 -> 'z', 1 -> 'y', etc.)
            mapped_char = chr(ord('z') - mod_val)
            
            result.append(mapped_char)
            
        return "".join(result)