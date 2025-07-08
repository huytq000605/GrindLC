/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* result;
        auto dfs = [&](this auto &&dfs, TreeNode* u) {
            if(!u) return;
            dfs(u->left);
            if(u == p) result = p;
            if(p == result) result = u;
            dfs(u->right);
        };
        dfs(root);
        return result == p ? nullptr: result;
    }
};
