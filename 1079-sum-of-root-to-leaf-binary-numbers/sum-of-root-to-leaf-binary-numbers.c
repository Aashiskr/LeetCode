/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * struct TreeNode *left;
 * struct TreeNode *right;
 * };
 */

// Helper function DFS traversal ke liye
int dfs(struct TreeNode* node, int current_val) {
    if (node == NULL) {
        return 0;
    }
    
    // Nayi bit ko shift karke add kar rahe hain (Optimized way of: current_val * 2 + node->val)
    current_val = (current_val << 1) | node->val;
    
    // Agar leaf node hai (dono child NULL), toh current binary value return kardo
    if (node->left == NULL && node->right == NULL) {
        return current_val;
    }
    
    // Left aur Right subtrees se aane wale sums ko add kar do
    return dfs(node->left, current_val) + dfs(node->right, current_val);
}

// Main function jo LeetCode call karega
int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0); // Initial value 0 se start karenge
}