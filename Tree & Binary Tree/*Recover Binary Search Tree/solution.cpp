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
    void recoverTree(TreeNode* root) {
        TreeNode* prev = new TreeNode{INT_MIN};
        TreeNode *node1 = nullptr, *node2 = nullptr;
        auto dfs = [&](TreeNode* u, auto dfs_ref) -> void {
            if(u == nullptr) return;
            dfs_ref(u->left, dfs_ref);
            if(!node1 && prev->val > u->val) {
                node1 = prev;
            }
            if(node1 && prev->val > u->val) {
                node2 = u;
            }
            prev = u;
            dfs_ref(u->right, dfs_ref);
        };
        dfs(root, dfs);
        swap(node1->val, node2->val);
    }
};
