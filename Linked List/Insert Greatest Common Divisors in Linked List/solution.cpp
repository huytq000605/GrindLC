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
    int gcd(int u, int v) {
        if(u < v) swap(u, v);
        if(!v) return u;
        return gcd(v, u % v);
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* node = head;
        while(node && node->next) {
            node->next = new ListNode(gcd(node->val, node->next->val), node->next);
            node = node->next->next;
        }
        return head;
    }
};
