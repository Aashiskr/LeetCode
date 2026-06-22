class Solution(object):
    def maxNumberOfBalloons(self, text):
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2  # 'l' do baar lagta hai isliye 2 se integer division
        o = text.count('o') // 2  # 'o' do baar lagta hai isliye 2 se integer division
        n = text.count('n')

        return min(b,a,l,o,n)
                    

        