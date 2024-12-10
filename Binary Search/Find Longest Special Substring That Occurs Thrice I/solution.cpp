class Solution {
public:
    int maximumLength(string s) {
        int lo{0}, hi = static_cast<int>(s.size());
        auto valid = [&](int target) -> bool {
            vector<int> count(26, 0);
            int cur{0};
            for(int i = 0; i < s.size(); ++i) {
                if(i == 0 || s[i] == s[i-1]) ++cur;
                else cur = 1;
                if(cur == target) {
                    if(++count[s[i] - 'a'] == 3) return true;
                    --cur;
                }
            }
            return false;
        };
        while(lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if(valid(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo ? lo: -1;
    }
};
