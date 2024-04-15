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

    vector<int> getLonelyNodes(TreeNode* root) {
        stack<TreeNode*> st;
        if(root != nullptr) st.push(root);
        vector<int> result;
        while(st.size()) {
            auto node = st.top();
            st.pop();
            if(node->left == nullptr || node->right == nullptr) {
                if(node->left != nullptr) result.push_back(node->left->val);
                if(node->right != nullptr) result.push_back(node->right->val);
            }
            if(node->left != nullptr) st.push(node->left);
            if(node->right != nullptr) st.push(node->right);
        }
        return result;    
    }
};
