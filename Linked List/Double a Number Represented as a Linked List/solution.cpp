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
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        while(head != nullptr) {
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    ListNode* doubleIt(ListNode* head) {
        head = reverse(head);
        int rem = 0;
        ListNode* node = head;
        while(node != nullptr) {
            node->val = node->val * 2 + rem;
            rem = node->val / 10;
            node->val %= 10;
            if(rem && node->next == nullptr) {
                node->next = new ListNode(1);
                break;
            }
            node = node->next;
        }
        
        return reverse(head);
    }
};
