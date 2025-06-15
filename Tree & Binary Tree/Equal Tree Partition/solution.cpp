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
    bool checkEqualTree(TreeNode* root) {
        unordered_set<int> s;
        auto dfs = [&](this auto &&dfs, TreeNode* u) {
            if(u == nullptr) return 0;
            int sleft = dfs(u->left);
            int sright = dfs(u->right);
            if(u != root) s.emplace(sleft + sright + u->val);
            return sleft + sright + u->val;
        };
        int total = dfs(root);
        return !(total & 1) && s.find(total / 2) != s.end();
    }
};
