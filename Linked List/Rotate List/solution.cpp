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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !k) return head;
        int n = 0;
        auto p = head;
        while(p) {
            p = p->next;
            n++;
        }

        k %= n;
        if(!k) return head;
        p = head;
        for(int i = 0; i < n-k-1; ++i) {
            p = p->next;
        }
        auto new_head = p->next;
        p->next = nullptr;
        p = new_head;
        while(p->next != nullptr) {
            p = p->next;
        }
        p->next = head;
        return new_head;
    }
};
