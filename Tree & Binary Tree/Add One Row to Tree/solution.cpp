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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if(depth == 1) return new TreeNode(val, root, nullptr);
        deque<TreeNode*> dq;
        dq.push_back(root);
        while(dq.size()) {
            int sz = dq.size();
            depth -= 1;
            for(int i = 0; i < sz; i++) {
                auto node = dq.front();
                dq.pop_front();
                if(depth == 1) {
                    node->left = new TreeNode(val, node->left, nullptr);
                    node->right = new TreeNode(val, nullptr, node->right);
                } else {
                    if(node->left != nullptr) dq.push_back(node->left);
                    if(node->right != nullptr) dq.push_back(node->right);
                }
            }
        }
        return root;
    }
};
