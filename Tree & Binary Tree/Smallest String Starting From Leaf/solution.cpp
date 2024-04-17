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
    void dfs(TreeNode* node, string cur, string & result) {
        cur += string(1, 'a' + node->val);
        if(node->left == nullptr && node->right == nullptr) {
            reverse(cur.begin(), cur.end());
            if(result == "" || cur < result) {
                result = cur;
            }
            return;
        }
        if(node->left != nullptr) dfs(node->left, cur, result);
        if(node->right != nullptr) dfs(node->right, cur, result);
    }
    string smallestFromLeaf(TreeNode* root) {
        string result = "";
        dfs(root, "", result);
        return result;
    }
};
