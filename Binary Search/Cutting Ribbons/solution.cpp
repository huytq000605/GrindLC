class Solution {
public:
    int maxLength(vector<int>& ribbons, int k) {
        long long lo{0}, hi{*max_element(ribbons.begin(), ribbons.end())};
        while(lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            long long l{};
            for(auto &r: ribbons) {
                l += r / mid;
            }
            if(l < k) {
                hi = mid-1;
            } else {
                lo = mid;
            }
        }
        return lo;
    }
};
