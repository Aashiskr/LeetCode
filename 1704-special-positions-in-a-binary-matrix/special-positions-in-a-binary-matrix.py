class Solution(object):
    def numSpecial(self, mat):
        ans = 0
        m = len(mat)    # Total rows
        n = len(mat[0]) # Total columns
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    # Check karein ki kya is row mein sirf ek hi '1' hai
                    if mat[r].count(1) == 1:
                        # Ab is column mein check karein
                        # List comprehension se poore column ka sum nikal lenge
                        col_sum = sum(mat[i][c] for i in range(m))
                        if col_sum == 1:
                            ans += 1
                            
        return ans