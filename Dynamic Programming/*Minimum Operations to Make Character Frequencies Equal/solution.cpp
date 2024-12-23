class Solution {
public:
    int makeStringGood(string s) {
        int mx{};
        unordered_map<int, int> counter;
        for(char c: s) {
            counter[c-'a']++;
            mx = max(mx, counter[c-'a']);
        }

        int result{INT_MAX};
        for(int target{}; target <= mx; ++target) {
            // dp1 is number of operations if previous character is deleted
            // dp2 is number of operations if previous character is inserted
            int dp1{}, dp2{}, deleted{};
            for(int i{}; i < 26; ++i) {
                int ndp1{}, ndp2{}, ndeleted{};
                if(counter[i] < target) {
                    ndp1 = min(dp1, dp2) + counter[i];
                    ndeleted = counter[i];
                    ndp2 = dp1 + max(0, target - counter[i] - deleted);
                    ndp2 = min(ndp2, dp2 + target - counter[i]);
                } else {
                    ndp1 = min(dp1, dp2) + (counter[i] - target);
                    ndeleted = counter[i] - target;
                    ndp2 = ndp1;
                }
                dp1 = ndp1;
                dp2 = ndp2;
                deleted = ndeleted;
            }
            result = min(result, min(dp1, dp2));
        }
        return result;
    }
};
