class Solution {
    using ll = long long;
    bool valid(vector<ll>& A, int side, int k, ll d) {
        for(int i{}; i < A.size(); ++i) {
            ll cur = A[i];
            ll max_end = 4ll*side - (d-A[i]);
            bool ok = true;
            for(int j{}; j < k-1; ++j) {
                auto nxt = lower_bound(A.begin(), A.end(), cur + d);
                if(nxt == A.end() || *nxt > max_end) {
                    ok = false;
                    break;
                }
                cur = *nxt;
            }
            if(ok) return true;
        }
        return false;
    }
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        vector<ll> A;
        for(auto &point: points) {
            long long x = point[0], y = point[1];
            if(x == 0) {
                A.emplace_back(y);
            } else if(y == side) {
                A.emplace_back(y + x);
            } else if(x == side) {
                A.emplace_back(2ll * side + (side - y));
            } else {
                A.emplace_back(3ll*side + (side - x));
            }
        }
        sort(A.begin(), A.end());
        long long lo = 1, hi = 4ll*side;
        while(lo < hi) {
            long long m = lo + (hi - lo + 1) / 2;
            if(valid(A, side, k, m)) {
                lo = m;
            } else {
                hi = m-1;
            }
        }
        return lo;
    }
};
