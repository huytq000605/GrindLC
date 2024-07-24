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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        set<int> A(nums.begin(), nums.end());
        ListNode* sentinal = new ListNode(0, head);
        ListNode* prev;
        head = sentinal;
        while(head != nullptr) {
            while(head->next != nullptr && A.find(head->next->val) != A.end()) {
                head->next = head->next->next;
            }
            prev = head;
            head = head->next;
        }
        return sentinal->next;
    }
};
