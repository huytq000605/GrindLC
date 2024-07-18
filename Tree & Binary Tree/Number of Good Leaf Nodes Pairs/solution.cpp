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
    int countPairs(TreeNode* root, int distance) {
        int result = 0;
        auto dfs = [distance, &result](TreeNode* u, auto dfs_ref) -> vector<int> {
            if(u == nullptr) return {};
            if(u->left == nullptr && u->right == nullptr) return {1};
            auto lefts = dfs_ref(u->left, dfs_ref);
            auto rights = dfs_ref(u->right, dfs_ref);
            for(auto l: lefts) {
                for(auto r: rights) {
                    if(l + r <= distance) {
                        result++;
                    }
                }
            }
            vector<int> leafs;
            for(auto l: lefts) if(l+1 < distance) leafs.emplace_back(l+1);
            for(auto r: rights) if(r+1 < distance) leafs.emplace_back(r+1);
            return leafs;
        };
        dfs(root, dfs);
        return result;
    }
};
