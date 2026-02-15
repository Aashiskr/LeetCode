class Solution(object):
    def addBinary(self, a, b):
        ss = int(a) + int(b)
        s = list(str(ss))
        l = len(s)
        
        for i in range(l - 1, 0, -1):
            d = int(s[i]) // 2
            if d != 0:
                r = int(s[i]) % 2
                s[i] = str(r)
                s[i-1] = str(int(s[i-1]) + d)

        first_digit = int(s[0])
        if first_digit >= 2:
            s[0] = str(first_digit % 2)
            s.insert(0, str(first_digit // 2))
        
        return "".join(s)