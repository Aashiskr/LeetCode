# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 1. Collect all nodes in sorted order using In-order Traversal
        sorted_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        # 2. Helper function to build a balanced BST from the sorted list
        def build_balanced(left, right):
            if left > right:
                return None
            
            # Choose the middle element to be the root
            mid = (left + right) // 2
            node = sorted_nodes[mid]
            
            # Recursively build the left and right subtrees
            node.left = build_balanced(left, mid - 1)
            node.right = build_balanced(mid + 1, right)
            
            return node
            
        return build_balanced(0, len(sorted_nodes) - 1)