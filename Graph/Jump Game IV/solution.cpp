class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, vector<int>> idxs;
        for(int i = 0; i < n; ++i) {
            idxs[arr[i]].push_back(i);
        }
        vector<bool> dp(n, false);
        dp[0] = true;
        deque<pair<int, int>> dq{{0, 0}};
        while(!dq.empty()) {
            auto [i, s] = dq.front(); dq.pop_front();
            if(i == n-1) return s;
            if(i && !dp[i-1]) {
                dp[i-1] = true;
                dq.emplace_back(i-1, s+1);
            }
            if(i+1 < n && !dp[i+1]) {
                dp[i+1] = true;
                dq.emplace_back(i+1, s+1);
            }
            for(auto j: idxs[arr[i]]) {
                if(!dp[j]) {
                    dp[j] = true;
                    dq.emplace_back(j, s+1);
                }
            }
            idxs[arr[i]] = {};
        }
        return -1;
    }
};
