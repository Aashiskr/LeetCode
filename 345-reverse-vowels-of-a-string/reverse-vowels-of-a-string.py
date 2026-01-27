class Solution(object):
    def reverseVowels(self, s):
        word = list(s)
        a = []  # list to store vowels
        vowels = "aeiouAEIOU"

        # Step 1: collect vowels
        for i in word:
            for j in vowels:
                if i == j:
                    a.append(i)
                    break

        # Step 2: replace vowels in reverse order
        idx = len(a) - 1
        for i in range(len(word)):
            if word[i] in vowels:
                word[i] = a[idx]
                idx -= 1

        return "".join(word)
