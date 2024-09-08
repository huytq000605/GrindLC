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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ListNode* cur = head;
        int n = 0;
        while(cur) {
            n++;
            cur = cur->next;
        }
        int each = n / k;
        int mod = n % k;
        vector<ListNode*> result(k);
        for(int i = 0; i < k && head; i++) {
            result[i] = head;
            for(int j = 0; j < each + (i < mod) - 1; j++) {
                head = head->next;
            }
            auto nxt = head->next;
            head->next = nullptr;
            head = nxt;
        }
        return result;
    }
};
