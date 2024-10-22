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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        vector<TreeNode*> q{root};
        while(!q.empty()) {
            long long s = 0;
            vector<TreeNode*> nq;
            for(auto node: q) {
                s += node->val;
                if(node->left) nq.emplace_back(node->left);
                if(node->right) nq.emplace_back(node->right);
            }
            swap(nq, q);
            pq.emplace(s);
            if(pq.size() > k) pq.pop();
        }
        return pq.size() == k ? pq.top() : -1ll;
    }
};
