VOWELS = set("aeiouAEIOU")

class Solution(object):
    def reverseVowels(self, s):
        lst = list(s)
        i, j = 0, len(lst) - 1

        while i < j:
            if lst[i] not in VOWELS:
                i += 1
            elif lst[j] not in VOWELS:
                j -= 1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        return "".join(lst)
