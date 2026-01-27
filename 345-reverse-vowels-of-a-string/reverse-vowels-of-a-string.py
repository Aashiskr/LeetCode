V = {'a','e','i','o','u','A','E','I','O','U'}

class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in V:
                i += 1
            elif s[j] not in V:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
