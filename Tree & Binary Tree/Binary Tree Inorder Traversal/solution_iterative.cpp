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
    vector<int> inorderTraversal(TreeNode* root) {
        if(root == nullptr) return {};
        vector<int> result;
        stack<TreeNode*> st;
        while(root != nullptr) {
            st.push(root);
            root = root->left;
        }
        while(st.size() > 0) {
            auto cur = st.top();
            st.pop();
            result.push_back(cur->val);
            cur = cur->right;
            while(cur != nullptr) {
                st.push(cur);
                cur = cur->left;
            }
        }
        return result;
    }
};
