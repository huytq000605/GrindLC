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
class FindElements {
unordered_set<int> s;
    void build(TreeNode* node) {
        s.emplace(node->val);
        if(node->left != nullptr) {      
            node->left->val = node->val * 2 + 1;
            build(node->left);
        }
        if(node->right != nullptr) {
            node->right->val = node->val * 2 + 2;
            build(node->right);
        }
    }
public:
    FindElements(TreeNode* root) {
        root->val = 0;
        build(root);
    }
    
    bool find(int target) {
        return s.find(target) != s.end();
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
