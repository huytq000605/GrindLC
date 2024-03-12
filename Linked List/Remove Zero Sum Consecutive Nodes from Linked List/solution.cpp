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
    ListNode* removeZeroSumSublists(ListNode* head) {
        std::unordered_map<int, ListNode*> prefixes;
        int prefix = 0;
        ListNode* dummy = new ListNode(0, head);
        ListNode* ptr = dummy;
        while(ptr) {
            prefix += ptr->val;
            auto prev = prefixes.find(prefix);
            if(prev != prefixes.end()) {
                ptr = prev->second->next;
                int prev_prefix = prefix + ptr->val;
                while(prev_prefix != prefix) {
                    prefixes.erase(prefixes.find(prev_prefix));
                    ptr = ptr->next;
                    prev_prefix += ptr->val;
                }
                prefixes.find(prefix)->second->next = ptr->next;
            } else {
                prefixes.emplace(prefix, ptr);
            }
            ptr = ptr->next;
        }
        return dummy->next;
    }
};
