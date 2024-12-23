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
    int minimumOperations(TreeNode* root) {
        int result{};
        deque<TreeNode*> dq;
        dq.emplace_back(root);
        while(!dq.empty()) {
            int l = dq.size();
            vector<int> values, ids(l);
            while(l--) {
                TreeNode* u = dq.front(); dq.pop_front();
                values.emplace_back(u->val);
                if(u->left) dq.emplace_back(u->left);
                if(u->right) dq.emplace_back(u->right);
            }
            iota(ids.begin(), ids.end(), 0);
            sort(ids.begin(), ids.end(), [&](int i1, int i2) -> bool {
                return values[i1] < values[i2];
            });
            for(int i{}; i < values.size(); ++i) {
                while(ids[i] != i) {
                    swap(ids[i], ids[ids[i]]);
                    ++result;
                }
            }
        }
        return result;
    }
};
