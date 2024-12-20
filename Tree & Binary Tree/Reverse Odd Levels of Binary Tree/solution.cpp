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
    TreeNode* reverseOddLevels(TreeNode* root) {
        int l{};
        deque<TreeNode*> dq;
        dq.emplace_back(root);
        while(!dq.empty()) {
            int t = dq.size();
            for(int i{}; i < t; ++i) {
                auto u = dq.front();
                dq.pop_front();
                if(u->left) dq.emplace_back(u->left);
                if(u->right) dq.emplace_back(u->right);
            }
            if(!(l&1)) {
                for(int i{}; i < static_cast<int>(dq.size()) / 2; ++i) {
                    swap(dq[i]->val, dq[dq.size()-1-i]->val);
                }
            }
            ++l;
        }
        return root;
    }
};
