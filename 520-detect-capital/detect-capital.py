class Solution(object):
    def detectCapitalUse(self, word):
        list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if word[0] in list1:
            
            x = 0
            l = len(word)
            for i in word:
                if i in list1:
                    x = x+1
            if x == 1 and word[0] in list1:
                return True
            if x == l:
                return True
            else:
                return False
            
        if word[0] in list2:
            x = 0
            l = len(word)
            for i in word:
                if i in list2:
                    x = x+1
            if x == l:
                return True
            else:
                return False

        

        