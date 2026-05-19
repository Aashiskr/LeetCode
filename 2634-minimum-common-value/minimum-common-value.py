class Solution(object):
    def getCommon(self, nums1, nums2):
        i, j = 0, 0
        
        # Traverse both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]  # Found the smallest common value
            elif nums1[i] < nums2[j]:
                i += 1  # Move the pointer of the smaller value
            else:
                j += 1  # Move the pointer of the smaller value
                
        return -1  # Return -1 if no common element exists