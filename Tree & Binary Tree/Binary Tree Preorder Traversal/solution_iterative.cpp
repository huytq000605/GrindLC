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
    vector<int> preorderTraversal(TreeNode* root) {
        if(root == nullptr) return {};
        stack<TreeNode*> st;
        st.push(root);
        vector<int> result;
        while(st.size() > 0) {
            TreeNode* node = st.top();
            st.pop();
            result.push_back(node->val);
            if(node->right != nullptr) {
                st.push(node->right);
            }
            if(node->left != nullptr) {
                st.push(node->left);
            }
        }
        return result;
    }
};
