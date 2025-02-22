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
    void parse(int val, int depth, vector<TreeNode*>& st, TreeNode** root) {
        while(depth != st.size()) st.pop_back();
        auto node = st.empty() ? nullptr: st.back();
        auto new_node = new TreeNode(val);
        st.emplace_back(new_node);
        if(!node) {
            *root = new_node;
        } else if(!node->left) {
            node->left = new_node;
        } else {
            node->right = new_node;
        }
    }
public:
    TreeNode* recoverFromPreorder(string traversal) {
        TreeNode* root = nullptr;
        vector<TreeNode*> st;
        int val{}, depth{};
        for(char c: traversal) {
            if(isdigit(c)) {
                val = val * 10 + (c - '0');
            } else {
                if(val) {
                    parse(val, depth, st, &root);
                    depth = 0;
                }
                val = 0;
                ++depth;
            }
        }
        parse(val, depth, st, &root);
        return root;
    }
};
