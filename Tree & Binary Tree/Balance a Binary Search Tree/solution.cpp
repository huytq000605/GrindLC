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
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> values;
        vector<TreeNode*> st;
        while(!st.empty() || root) {
            while(root) {
                st.push_back(root);
                root = root->left;
            }
            root = st.back(); st.pop_back();
            values.push_back(root->val);
            root = root->right;
        }
        auto build = [&](this auto&& build, int l, int r) -> TreeNode* {
            if(l == r) {
                return new TreeNode(values[l]);
            }
            if(l > r) return nullptr;
            int m = l + (r-l) / 2;
            auto ret = new TreeNode(values[m]);
            ret->left = build(l, m-1);
            ret->right = build(m+1, r);
            return ret;
        };
        return build(0, values.size() - 1);

    }
};
