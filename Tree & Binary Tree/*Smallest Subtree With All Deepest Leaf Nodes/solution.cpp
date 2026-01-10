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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        auto dfs = [&](this auto&& dfs, TreeNode* u) -> pair<int, TreeNode*> {
            if(u == nullptr) return {0, nullptr};
            auto [d1, left] = dfs(u->left);
            auto [d2, right] = dfs(u->right);
            return {max(d1, d2) + 1, d1 == d2 ? u : d1 > d2 ? left: right};
        };
        return dfs(root).second;
    }
};
