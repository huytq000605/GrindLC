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
    int maxProduct(TreeNode* root) {
        long long s = 0;
        vector<TreeNode*> vs{root};
        while(!vs.empty()) {
            auto u = vs.back(); vs.pop_back();
            s += u->val;
            if(u->left) vs.push_back(u->left);
            if(u->right) vs.push_back(u->right);
        }
        long long result = 0;
        auto dfs = [s, &result](this auto&& dfs, TreeNode* u) -> long long {
            if(u == nullptr) return 0;
            long long ret = dfs(u->left) + dfs(u->right) + u->val;
            result = max(result, ret * (s - ret));
            return ret;
        };
        dfs(root);
        return result % int(1e9 + 7);
    }
};
