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
    vector<int> result;

    void dfs(TreeNode* node) {
        if(node == nullptr) return;
        if(node->left == nullptr || node->right == nullptr) {
            if(node->left != nullptr) result.push_back(node->left->val);
            if(node->right != nullptr) result.push_back(node->right->val);
        }
        dfs(node->left);
        dfs(node->right);
    }

    vector<int> getLonelyNodes(TreeNode* root) {
        dfs(root);
        return result;    
    }
};
