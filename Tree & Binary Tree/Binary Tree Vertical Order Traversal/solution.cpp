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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> cols(201);
        deque<pair<TreeNode*, int>> dq{{root, 100}};
        int mn_col = 201, mx_col = 0;
        while(!dq.empty()) {
            auto [u, c] = dq.front(); dq.pop_front();
            if(u == nullptr) continue;
            mn_col = min(mn_col, c);
            mx_col = max(mx_col, c);
            cols[c].push_back(u->val);
            dq.emplace_back(u->left, c-1);
            dq.emplace_back(u->right, c+1);
        }
        vector<vector<int>> result;
        for(int col = mn_col; col <= mx_col; ++col) {
            result.push_back(move(cols[col]));
        }
        return result;
    }
};
