class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            # Calculate the sum of elements to the right
            right_sum = total_sum - left_sum - num
            
            # Calculate absolute difference and add to answer
            answer.append(abs(left_sum - right_sum))
            
            # Update left sum for the next iteration
            left_sum += num
            
        return answer