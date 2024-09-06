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
        ListNode* dummy = new ListNode(0, head);
        head = dummy;
        unordered_set<int> s(nums.begin(), nums.end());
        while(head) {
            while(head->next && s.find(head->next->val) != s.end()) {
                head->next = head->next->next;
            }
            head = head->next;
        }
        return dummy->next;
    }
};
