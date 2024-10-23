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
    TreeNode* replaceValueInTree(TreeNode* root) {
        deque<pair<TreeNode*, int>> dq{{root, 0}};
        int s = root->val;
        while(!dq.empty()) {
            int sz = dq.size();
            int ns = 0;
            for(int i = 0; i < sz; ++i) {
                auto [u, v] = dq.front();
                dq.pop_front();
                u->val = s - u->val - v;
                if(u->left) {
                    dq.emplace_back(u->left, u->right ? u->right->val : 0);
                    ns += u->left->val;
                }
                if(u->right) {
                    dq.emplace_back(u->right, u->left ? u->left->val: 0);
                    ns += u->right->val;
                }
            }
            swap(s, ns);
        }
        return root;
    }
};
