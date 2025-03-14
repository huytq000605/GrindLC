class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        int lo = 0, hi = *max_element(candies.begin(), candies.end());
        while(lo < hi) {
            int m = lo + (hi - lo + 1) / 2;
            long long gave = 0;
            for(int candy: candies) {
                gave += candy / m;
                if(gave >= k) break;
            }
            if(gave >= k) {
                lo = m;
            } else {
                hi = m-1;
            }
        }
        return lo;
    }
};
