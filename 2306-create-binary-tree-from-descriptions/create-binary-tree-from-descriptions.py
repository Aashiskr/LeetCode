# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()
        
        # Build the tree and track all children
        for parent_val, child_val, is_left in descriptions:
            # Create the parent node if it hasn't been created yet
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
                
            # Create the child node if it hasn't been created yet
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Link the child to the parent
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Add the child's value to our set to keep track of it
            children.add(child_val)
            
        # The root is the only node that is never a child
        for val in nodes:
            if val not in children:
                return nodes[val]
                
        return None