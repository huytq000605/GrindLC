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
    void reorderList(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while(fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode *next_slow = slow->next;
        slow->next = NULL;
        slow = reverse(next_slow);
        while(slow) {
            ListNode *next = head->next;
            ListNode *next_slow = slow->next;
            head->next = slow;
            slow->next = next;
            head = next;
            slow = next_slow;
        }
    }

    ListNode* reverse(ListNode* head) {
        ListNode *prev = NULL;
        while(head) {
            ListNode *next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
};
