class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> next_higher(n, n), prev_higher(n, n);
        vector<int> st;
        for(int i = 0; i < n; ++i) {
            while(!st.empty() && i - st.back() <= d && arr[i] > arr[st.back()]) {
                int j = st.back(); st.pop_back();
                next_higher[j] = i;
            }
            st.push_back(i);
        }
        st.clear();
        for(int i = n-1; i >= 0; --i) {
            while(!st.empty() && st.back() - i <= d && arr[i] > arr[st.back()]) {
                int j = st.back(); st.pop_back();
                prev_higher[j] = i;
            }
            st.push_back(i);
        }
        vector<int> dp(n, -1);
        auto dfs = [&](this auto& dfs, int u) {
            if(u == n) return 0;
            if(dp[u] != -1) return dp[u];
            return dp[u] = 1 + max(dfs(next_higher[u]), dfs(prev_higher[u]));
        };
        for(int i = 0; i < n; ++i) dfs(i);
        return *max_element(begin(dp), end(dp));
    }
};
