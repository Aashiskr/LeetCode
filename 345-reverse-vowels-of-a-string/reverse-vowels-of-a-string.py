S = set("aeiouAEIOU")

class Solution(object):
    def reverseVowels(self, s):
        i, j, lst = 0, len(s) - 1, list(s)
        while i < j:
            while i < j and lst[i] not in S: i += 1
            while i < j and lst[j] not in S: j -= 1
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        return "".join(lst)