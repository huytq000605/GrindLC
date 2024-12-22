/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        bool havep{}, haveq{};
        function<TreeNode*(TreeNode*)> dfs = [&](TreeNode* u) -> TreeNode* {
            if(!u) return nullptr;
            if(u == p) havep = true;
            if(u == q) haveq = true;
            auto left = dfs(u->left);
            auto right = dfs(u->right);
            if(left && right) return u;
            if(u == p || u == q) return u;
            return left ? left: right;
        };
        auto res = dfs(root);
        if(havep && haveq) return res;
        return nullptr;
    }
};
