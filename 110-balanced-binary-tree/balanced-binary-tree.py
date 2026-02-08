# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        # Helper function jo height return karega
        # Agar unbalanced hai toh -1 return karega
        def check_height(node):
            if not node:
                return 0
            
            # Left subtree check karo
            left_h = check_height(node.left)
            if left_h == -1: 
                return -1
            
            # Right subtree check karo
            right_h = check_height(node.right)
            if right_h == -1: 
                return -1
            
            # Agar difference 1 se zyada hai -> Unbalanced
            if abs(left_h - right_h) > 1:
                return -1
            
            # Height return karo
            return max(left_h, right_h) + 1
            
        # Agar check_height -1 return kare toh False, nahi toh True
        return check_height(root) != -1