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
    int sumRootToLeaf(TreeNode* root) {
        int result = 0;
        auto dfs = [&result](this auto&& dfs, TreeNode* u, int mask) {
            if(u == nullptr) return;
            mask = (mask << 1) | u->val;
            if(u->left || u->right) {
                dfs(u->left, mask);
                dfs(u->right, mask);
            } else {
                result += mask;
            }
        };
        dfs(root, 0);
        return result;
    }
};
