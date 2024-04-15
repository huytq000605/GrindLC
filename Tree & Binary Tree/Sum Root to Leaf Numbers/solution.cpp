/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dfs(TreeNode* node, int v) {
        if(node == nullptr) return 0;
        v = v * 10 + node->val;
        if(node->left == nullptr && node->right == nullptr) return v;
        return dfs(node->left, v) + dfs(node->right, v);
    }
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);      
    }
};
