class Solution:
    def mergeAlternately(self, word1, word2):
        i = 0
        merge = []

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])
            i += 1

        return "".join(merge)
