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
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        map<int, vector<pair<int, int>>> cousins;
        map<int, int> depths;
        auto cmp = [](auto p1, auto p2) -> bool {
            return p1.second > p2.second;
        };
        auto dfs = [&](TreeNode* u, int depth, auto dfs) -> int {
            if(!u) return 0;
            depths[u->val] = depth;
            int l = dfs(u->left, depth+1, dfs);
            int r = dfs(u->right, depth+1, dfs);
            int childs = max(l, r) + 1;
            cousins[depth].emplace_back(u->val, childs);
            push_heap(cousins[depth].begin(), cousins[depth].end(), cmp);
            if(cousins[depth].size() > 2) {
                pop_heap(cousins[depth].begin(), cousins[depth].end(), cmp);
                cousins[depth].pop_back();
            }
            return childs;
        };
        dfs(root, 0, dfs);
        vector<int> result;
        for(int u: queries) {
            int depth = depths[u];
            int mx_child = 0;
        
            for(auto [v, child]: cousins[depth]) {
                if(v != u) {
                    mx_child = child;
                } 
            }
            result.emplace_back(depth + mx_child - 1);
        }
        return result;
    }
};
