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
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        vector<int> lps = {0};
        vector<int> A = {head->val};
        int i = 0;
        ListNode* node = head->next;
        while(node) {
            while(i && node->val != A[i]) {
                i = lps[i-1];
            }
            i += node->val == A[i];
            lps.emplace_back(i);
            A.emplace_back(node->val);
            node = node->next;
        }
        auto dfs = [&](TreeNode* node, int i, auto dfs_ref) -> bool {
            if(!node) return false;
            while(i && node->val != A[i]) {
                i = lps[i-1];
            }
            i += node->val == A[i];
            return i == A.size() || dfs_ref(node->left, i, dfs_ref) || dfs_ref(node->right, i, dfs_ref);
        };
        return dfs(root, 0, dfs);
    }
};
