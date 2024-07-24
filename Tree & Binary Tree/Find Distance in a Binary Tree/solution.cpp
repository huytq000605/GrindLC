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
    int findDistance(TreeNode* root, int p, int q) {
        if(p == q) return 0;
        // dfs returns a pair of <distance from p or q, we found the lca p & q> 
        auto dfs = [&](TreeNode* u, auto dfs_ref) -> pair<int, bool> {
            if(u == nullptr) return make_pair(0, false);
            // if already found lca, just pop up the result
            auto left = dfs_ref(u->left, dfs_ref);
            if(left.second) return left;
            auto right = dfs_ref(u->right, dfs_ref);
            if(right.second) return right;

            int lv = left.first, rv = right.first;
        
            if(u->val == p || u->val == q) {
                // p or q is lca of p and q
                if(lv || rv) {
                    return make_pair(lv + rv, true);
                }
                // if u is p or q, return the distance as 1
                return make_pair(1, false);
            }
            // found lca of p and q
            if(lv && rv) {
                return make_pair(lv + rv, true);
            }
            // return up the distance
            if(lv || rv) return make_pair(lv + rv + 1, false);
            return make_pair(0, false);
        };

        return dfs(root, dfs).first;
    }
};
