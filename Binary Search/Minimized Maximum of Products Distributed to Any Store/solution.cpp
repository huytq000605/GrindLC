class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int lo = 1, hi = *max_element(quantities.begin(), quantities.end());
        while(lo < hi) {
            int mid = lo + (hi - lo)/2;
            int used{};
            for(int q: quantities) {
                used += (q + mid - 1) / mid;
                if(used > n) break;
            }
            if(used <= n) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
