class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        sort(power.begin(), power.end());
        deque<pair<long long, int>> dq;
        long long mx = 0;
        for(int p: power) {
            if(!dq.empty() && dq.back().second == p) {
                dq.back().first += p;
            } else {
                while(!dq.empty() && dq.front().second + 2 < p) {
                    mx = max(mx, dq.front().first);
                    dq.pop_front();
                }
                dq.emplace_back(mx + p, p);
            }
        }
        long long result = 0;
        for(auto [p, _]: dq) {
            result = max(result, p);
        }
        return result;
    }
};
