class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        int n = stations.size();
        vector<long long> powers(n);
        long long power = accumulate(stations.begin(), stations.begin() + r, 0ll);
        long long lo = 0, hi = power;
        for(int i = 0; i < stations.size(); ++i) {
            if(i + r < n) power += stations[i+r];
            if(i-r-1 >= 0) power -= stations[i-r-1];
            hi = max(hi, power);
            powers[i] = power;
        }
        hi += k;
        
        while(lo < hi) {
            long long mi = lo + (hi - lo + 1) / 2;
            bool valid = true;
            deque<pair<int, int>> dq;
            for(long long i = 0, s = 0, m = 0; i < n; ++i) {
                while(!dq.empty() && i > dq.front().first) {
                    s -= dq.front().second;
                    dq.pop_front();
                }
                if(powers[i] + s < mi) {
                    long long d = mi - powers[i] - s;
                    m += d;
                    s += d;
                    dq.emplace_back(i+2*r, d);
                }
                if(m > k) {
                    valid = false;
                    break;
                }
            }
            if(!valid) {
                hi = mi - 1;
            } else {
                lo = mi;
            }
        }
        return lo;
    }
};
