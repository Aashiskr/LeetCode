class Solution(object):
    def arrayRankTransform(self, arr):
        # 1. Get unique elements and sort them
        sorted_unique = sorted(set(arr))
        
        # 2. Create a dictionary to map each number to its rank
        # Enumerate starts at index 0, so we add 1 for the rank
        rank_map = {}
        for index, num in enumerate(sorted_unique):
            rank_map[num] = index + 1
            
        # 3. Build the final result using the original array
        return [rank_map[num] for num in arr]