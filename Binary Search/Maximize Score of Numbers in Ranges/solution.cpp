class Solution {
public:
    int maxPossibleScore(vector<int>& start, int d) {
        sort(start.begin(), start.end());
        int n = start.size();
       
        auto valid = [&](long long score) -> bool {
            long long cur = 0;
            for(int i = 0; i < n-1; ++i) {
                long long s2 = start[i+1], e2 = s2 + d;
                cur = max(static_cast<long long>(start[i]), cur);
                if(cur + score > e2) return false;
                cur += score;
            }
            return true;
        };
        long long lo = 0, hi = pow(10, 9) * 2;       
        while(lo < hi) {
            long long mid = lo + (hi - lo + 2) / 2;
            if(valid(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
