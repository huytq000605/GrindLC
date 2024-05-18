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
    int distributeCoins(TreeNode* root) {
        int result = 0;
        auto dfs = [&](TreeNode* root) {
            auto dfs_ref = [&](TreeNode* root, auto dfs_ref) -> int {
                if(root == nullptr) return 0;
                int left = dfs_ref(root->left, dfs_ref);
                int right = dfs_ref(root->right, dfs_ref);
                result += abs(root->val + left + right - 1);
                return root->val + left + right - 1;
            };
            return dfs_ref(root, dfs_ref);
        };
        dfs(root);
        return result;
    }
};
