VOWELS = {'a','e','i','o','u','A','E','I','O','U'}

class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] in VOWELS and s[r] in VOWELS:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in VOWELS:
                    l += 1
                if s[r] not in VOWELS:
                    r -= 1

        return "".join(s)
