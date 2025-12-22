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
    int longestConsecutive(TreeNode* root) {
        int result = 0;
        auto dfs = [&result](this auto&& dfs, TreeNode* u) -> pair<int, int> {
            if(u == nullptr) return {0, 0};
            auto left = dfs(u->left);
            auto right = dfs(u->right);
            int left_inc = u->left && ((u->val + 1) == u->left->val) ? left.first: 0;
            int right_inc = u->right && ((u->val + 1) == u->right->val) ? right.first: 0;
            int left_dec = u->left && ((u->val - 1) == u->left->val) ? left.second: 0;
            int right_dec = u->right && ((u->val - 1) == u->right->val) ? right.second: 0;
            result = max(result, max(left_inc + right_dec + 1, left_dec + right_inc + 1));
            return {max(left_inc, right_inc) + 1, max(left_dec, right_dec) + 1};
        };
        dfs(root);
        return result;
    }
};
