class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base case: Agar string khali hai ya bahut choti, wapas bhej do
        if not s:
            return ""

        res = []
        count = 0  # 1 aur 0 ka balance check karne ke liye
        i = 0
        
        # 1. String ko independent "Special Substrings" mein split karo
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # Jab count 0 ho jaye, matlab ek complete special string mil gayi
            if count == 0:
                # '1' + [andar ka maal] + '0'
                # Andar wale part ko fir se solve (recurse) karo
                inner_part = s[i + 1 : j]
                res.append('1' + self.makeLargestSpecial(inner_part) + '0')
                i = j + 1
        
        # 2. Saare parts ko bade-se-chote order mein sort karo
        # Kyunki "1100" pehle aana chahiye "10" se taaki string badi bane
        res.sort(reverse=True)
        
        # 3. Sabko wapas jod kar string bana do
        return "".join(res)