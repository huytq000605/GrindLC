class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long lo = 1, hi = 1ll * ranks[0] * cars*cars;
        while(lo < hi) {
            long long m = lo + (hi - lo ) / 2;
            long long repaired = 0;
            for(auto r: ranks) {
                long long cap = floor(sqrt(m / r));
                repaired += cap;
                if(repaired >= cars) break;
            }
            if(repaired >= cars) {
                hi = m;
            } else {
                lo = m + 1;
            }
        }
        return lo;
    }
};
