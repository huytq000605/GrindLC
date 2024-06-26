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
    ListNode* removeNodes(ListNode* head) {
        stack<ListNode*> st;
        ListNode* ans = head;
        while(head != nullptr) {
            while(st.size() && st.top()->val < head->val) {
                st.pop();
            }
            if(st.size() == 0) {
                ans = head;
            } else {
                st.top()->next = head;
            }
            st.push(head);
            head = head->next;
        }
        return ans;
    }
};
