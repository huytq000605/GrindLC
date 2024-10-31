class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(factory.begin(), factory.end(), [](auto &v1, auto &v2) -> bool {
            return v1[0] < v2[0];
        });
        sort(robot.begin(), robot.end(), [](int r1, int r2) -> bool {
            return r1 < r2;
        });
        // dp[r][f] minium distances using r robots and f factories.
        vector<vector<long long>> dp(robot.size()+1, vector<long long>(factory.size()+1, LLONG_MAX));
        dp[0] = vector<long long>(factory.size()+1, 0);
        long long result = LLONG_MAX;
        for(int r = 1; r <= robot.size(); ++r) {
            for(int f = 1; f <= factory.size(); ++f) {
                // new factory might not be helpful, so the result is eq to dp[r][f-1]
                // can optimized to O(n) since dp[r][f] only depending on dp[r-k][f-1]
                dp[r][f] = dp[r][f-1];
                long long cost = 0;
                for(int k = 1; k <= min(factory[f-1][1], r); ++k) {
                    cost += abs(factory[f-1][0] - robot[r-k]); 
                    if(dp[r-k][f-1] == LLONG_MAX) continue;
                    dp[r][f] = min(dp[r][f], dp[r-k][f-1] + cost);
                }
            }
        }
        return dp[robot.size()][factory.size()];
    }
};
