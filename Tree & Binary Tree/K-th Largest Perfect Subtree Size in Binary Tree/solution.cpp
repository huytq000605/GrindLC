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
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        auto dfs = [&](TreeNode* node, auto dfs_ref) -> pair<bool, int> {
            if(!node) return {true, 0};
            auto [lp, ls] = dfs_ref(node->left, dfs_ref);
            auto [rp, rs] = dfs_ref(node->right, dfs_ref);
            if(!lp || !rp || ls != rs) return {false, 0};
            pq.emplace(ls+rs+1);
            if(pq.size() > k) pq.pop();
            return {true, ls+rs+1};
        };
        dfs(root, dfs);
        return pq.size() == k ? pq.top() : -1;
    }
};
