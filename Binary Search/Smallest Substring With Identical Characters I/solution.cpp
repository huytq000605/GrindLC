class Solution {
public:
    int minLength(string s, int numOps) {
        if(!numOps) {
            int result{};
            for(int i{}; i < s.size();) {
                int j{i+1};
                while(j < s.size() && s[j] == s[i]) ++j;
                result = max(result, j - i);
                i = j;
            }
            return result;
        }
        int lo{1}, hi = s.size();
        auto possible = [&](int target) {
            int ops{};
            if(target == 1) {
                int ops1{}, ops2{};
                for(int i{}; i < s.size(); ++i) {
                    ops1 += i % 2 ? s[i] == '0' : s[i] == '1';
                    ops2 += i % 2 ? s[i] == '1' : s[i] == '0';
                }
                ops = min(ops1, ops2);
            } else {
                for(int i{}; i < s.size();) {
                    int j{i+1};
                    while(j < s.size() && s[j] == s[i]) ++j;
                    if(j-i > target) ops += (j-i) / (target+1);
                    i = j;
                }
            }
            
            return ops <= numOps;
        };
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(possible(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
