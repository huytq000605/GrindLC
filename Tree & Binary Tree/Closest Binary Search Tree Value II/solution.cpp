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
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        deque<int> dq;
        auto dfs = [&](this auto&& dfs, TreeNode* u) -> void {
            if(!u) return;
            dfs(u->left);
            if(u->val <= target) {
                if(dq.size() < k) dq.emplace_back(u->val);
                else {
                    dq.pop_front();
                    dq.emplace_back(u->val);
                }
            } else {
                if(dq.size() < k) dq.emplace_back(u->val);
                else if(dq.front() < u->val && target - dq.front() > u->val - target) {
                    dq.pop_front();
                    dq.emplace_back(u->val);
                } else {
                    return;
                }
            }
            dfs(u->right);
        };
        dfs(root);
        return vector<int>(dq.begin(), dq.end());
    }
};
