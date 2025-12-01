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
    bool twoSumBSTs(TreeNode* r1, TreeNode* r2, int target) {
        vector<TreeNode*> s1, s2;
        while(true) {
            while(r1) {
                s1.push_back(r1);
                r1 = r1->left;
            }
            while(r2) {
                s2.push_back(r2);
                r2 = r2->right;
            }
            if(s1.empty() || s2.empty()) return false;
            auto t1 = s1.back(), t2 = s2.back();
            if(t1->val + t2->val == target) return true;
            else if(t1->val + t2->val < target) {
                s1.pop_back();
                r1 = t1->right;
            } else {
                s2.pop_back();
                r2 = t2->left;
            }
        }
        return false;
    }
};
