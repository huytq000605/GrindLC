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
    int averageOfSubtree(TreeNode* root) {
        int result = 0;
        auto dfs = [&result](this auto& dfs, TreeNode* u) -> pair<int, int> {
            if(u == nullptr) return {0, 0};
            auto left = dfs(u->left);
            auto right = dfs(u->right);
            int s = u->val + left.first + right.first;
            int n = 1 + left.second + right.second;
            if(s / n == u->val) {
                result++;
            }
            return {s, n};
        };
        dfs(root);
        return result;
    }
};
