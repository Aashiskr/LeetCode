class Solution(object):
    def reverseWords(self, s):
        word = s
        words = []
        w = ""
        
        for i in word:
            if i != " ":
                w = w + i
            elif i == " ":
                if w:
                    words.append(w)
                    w = ""
        
        if w:
            words.append(w)

        r = []
        l = len(words)
        for i in range(l - 1, -1, -1):
            r.append(words[i])

        return " ".join(r)


                
        