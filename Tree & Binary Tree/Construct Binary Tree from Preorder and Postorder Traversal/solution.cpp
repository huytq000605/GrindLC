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
vector<int> *pre, *post;
TreeNode* build(int i1, int i2, int j1, int j2) {
    if(i1 > i2) return nullptr;
    auto root = new TreeNode((*pre)[i1]);
    if(i1 == i2) return root;
    int v = (*pre)[i1+1];
    int left_size = find(post->begin()+j1, post->begin() + j2 + 1, v) - (post->begin() + j1) + 1;
    root->left = build(i1+1, i1+left_size, j1, j1+left_size-1);
    root->right = build(i1+left_size+1, i2, j1+left_size, j2-1);
    return root;
}
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        pre = &preorder;
        post = &postorder;
        return build(0, preorder.size()-1, 0, postorder.size()-1);
    }
};
