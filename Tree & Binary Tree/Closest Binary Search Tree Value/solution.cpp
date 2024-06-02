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
    int closestValue(TreeNode* root, double target) {
        int result = -1;
        auto dfs = [&](auto node, auto& dfs_ref) {
            if(node == nullptr) return;
            dfs_ref(node->left, dfs_ref);
            if(result == -1 || abs(target - node->val) < abs(target - result)) {
                result = node->val;
            }
            dfs_ref(node->right, dfs_ref);
        };
        dfs(root, dfs);
        return result;
    }
};
