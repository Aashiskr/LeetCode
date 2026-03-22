from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check all 4 possible rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            if mat == target:
                return True
            
            # Rotate the matrix 90 degrees clockwise
            mat = [list(row) for row in zip(*mat[::-1])]
            
        return False