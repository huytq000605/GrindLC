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
class Solution {
public:
    ListNode* deleteNodes(ListNode* head, int m, int n) {
        auto u = head;
        while(true && u) {
            for(int i = 0; i < m-1 && u; ++i) {
                u = u->next;
            }
            if(u == nullptr) break;
            auto p = u;
            for(int i = 0; i <= n && u; ++i) {
                u = u->next;
            }
            p->next = u;
        }
        return head;
    }
};
