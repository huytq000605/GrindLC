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
    int maxLevelSum(TreeNode* root) {
        deque<TreeNode*> dq;
        dq.push_back(root);
        int level = 1;
        int result = 1;
        int result_s = INT_MIN;
        while(!dq.empty()) {
            int n = dq.size();
            int s = 0;
            for(int i = 0; i < n; ++i) {
                auto u = dq.front(); dq.pop_front();
                s += u->val;
                if(u->left) dq.push_back(u->left);
                if(u->right) dq.push_back(u->right);
            }
            if(s > result_s) {
                result = level;
                result_s = s;
            }
            ++level;
        }
        return result;
    }
};
