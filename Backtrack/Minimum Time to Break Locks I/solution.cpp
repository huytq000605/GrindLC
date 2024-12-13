class Solution {
public:
    int findMinimumTime(vector<int>& strength, int K) {
        int n = static_cast<int>(strength.size());
        int X{1}, result{};
        auto dfs = [&](int mask, int X, auto dfs) -> int {
            if(mask == (1<<n) - 1) return 0;
            int result{INT_MAX};
            for(int i{}; i < n; ++i) {
                if(((mask >> i) & 1) == 0) {
                    result = min(result, (strength[i] + X - 1) / X + dfs(mask | (1 << i), X + K, dfs));
                }
            }
            return result;
        };
        return dfs(0, 1, dfs);
    }
};
