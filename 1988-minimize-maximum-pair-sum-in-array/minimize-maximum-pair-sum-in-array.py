class Solution(object):
    def minPairSum(self, nums):
        nums.sort()  # Array ko in-place sort kiya
        l = len(nums)
        j = []
        
        # 'x' ko loop ke bahar initialize karo taaki wo reset na ho
        x = -1 
        
        for i in range(l // 2):  # Array ke aadhe hisse tak chalenge
            a = nums[i] + nums[x]
            j.append(a)
            x = x - 1  # Peeche se ek step andar aao
            
        return max(j)  # Sabse bada pair sum return kar do