/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
private:
    bool is_sub(ListNode* head, TreeNode* root) {
        if(head && root) {
            if(head->val != root->val) return false;
            return is_sub(head->next, root->left) || is_sub(head->next, root->right);
        }
        if(head) return false;
        return true;
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        stack<TreeNode*> s;
        s.emplace(root);
        while(!s.empty()) {
            auto r = s.top();
            s.pop();
            if(is_sub(head, r)) return true;
            if(r->left) s.emplace(r->left);
            if(r->right) s.emplace(r->right);
        }
        return false;
    }
};
