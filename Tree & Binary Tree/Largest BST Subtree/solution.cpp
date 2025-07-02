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
    int largestBSTSubtree(TreeNode* root) {
        if(!root) return 0;
        int result = 0;
        auto dfs = [&](this auto&& dfs, TreeNode* u) -> tuple<int, int, int> {
            if(!u) return {INT_MAX, INT_MIN, 0};
            auto [left_lo, left_hi, nl] = dfs(u->left);
            auto [right_lo, right_hi, nr] = dfs(u->right);
            int n = 0;
            if(u->val > left_hi && u->val < right_lo) {
                n = 1 + nl + nr;
            } else {
                n = INT_MIN;
            }
            result = max(result, n);
            return {min(left_lo, u->val), max(right_hi, u->val), 1 + nl + nr};
        };
        dfs(root);
        return result;
    }
};
