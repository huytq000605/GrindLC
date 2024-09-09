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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> result(m, vector<int>(n, -1));
        int filled = m*n;
        int mnr = 0, mxr = m-1, mnc = 0, mxc = n-1;
        while(head && filled) {
            for(int r = mnr, c = mnc; c <= mxc && head; ++c) {
                result[r][c] = head->val;
                head = head->next;
                --filled;
            }
            for(int r = mnr+1, c = mxc; r <= mxr && head; ++r) {
                result[r][c] = head->val;
                head = head->next;
                --filled;
            }
            for(int r = mxr, c = mxc - 1; c >= mnc && head; --c) {
                result[r][c] = head->val;
                head = head->next;
                --filled;
            }
            for(int r = mxr-1, c = mnc; r > mnr && head; --r) {
                result[r][c] = head->val;
                head = head->next;
                --filled;
            }
            ++mnr;
            ++mnc;
            --mxc;
            --mxr;
        }
        return result;
    }
};
