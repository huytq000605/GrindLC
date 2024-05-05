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
    double maximumAverageSubtree(TreeNode* root) {
        auto dfs = [](TreeNode* u) -> double {
            double result = 0;
            auto dfs_ref = [&](TreeNode* u, auto dfs_ref) -> pair<int, int> {
                if(u == nullptr) return {0, 0};
                auto [ls, ln] = dfs_ref(u->left, dfs_ref);
                auto [rs, rn] = dfs_ref(u->right, dfs_ref);
                int s = ls + rs + u->val;
                int n = ln + rn + 1;
                result = max(result, double(s) / n);
                return {s, n};
            };
            dfs_ref(u, dfs_ref);
            return result;
        };
        return dfs(root);
    }
};
