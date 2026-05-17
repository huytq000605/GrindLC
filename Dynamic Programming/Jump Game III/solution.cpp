class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<bool> dp(n);
        dp[start] = true;
        deque<int> dq{start};
        while(!dq.empty()) {
            auto u = dq.front(); dq.pop_front();
            if(arr[u] == 0) return true;
            for(int v: {u + arr[u], u - arr[u]}) {
                if(v < 0 || v >= n) continue;
                if(dp[v]) continue;
                dq.push_back(v);
                dp[v] = true;
            }
        }
        return false;
    }
};
