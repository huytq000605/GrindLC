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
    vector<int> largestValues(TreeNode* root) {
        if(root == nullptr) return {};
        deque<TreeNode*> dq;
        dq.emplace_back(root);
        vector<int> result;
        while(!dq.empty()) {
            int k = dq.size();
            int mx{INT_MIN};
            while(k--) {
                TreeNode* u = dq.front(); dq.pop_front();
                mx = max(mx, u->val);
                if(u->left) dq.emplace_back(u->left);
                if(u->right) dq.emplace_back(u->right);
            }
            result.emplace_back(mx);
        }
        return result;
    }
};
