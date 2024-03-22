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
    bool isPalindrome(ListNode* head) {
        ListNode *prev = NULL, *slow = head, *fast = head;
        while(fast && fast->next) {
            fast = fast->next->next;

            ListNode *nxt = slow->next;
            slow->next = prev;
            prev = slow;
            slow = nxt;
        }
        if(fast) {
            slow = slow->next;
        }
        while(slow) {
            if(slow->val != prev->val) return false;
            slow = slow->next;
            prev = prev->next;
        }
        return true;

    }
};
