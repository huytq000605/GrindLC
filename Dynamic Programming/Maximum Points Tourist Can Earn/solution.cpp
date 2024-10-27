class Solution {
public:
    int maxScore(int n, int k, vector<vector<int>>& stayScore, vector<vector<int>>& travelScore) {
        vector<int> dp(n);
        for(int day = 0; day < k; ++day) {
            vector<int> ndp(n);
            for(int start = 0; start < n; ++start) {
                for(int dest = 0; dest < n; ++dest) {
                    if(start == dest) {
                        ndp[dest] = max(ndp[dest], dp[start] + stayScore[day][start]);
                    } else {
                        ndp[dest] = max(ndp[dest], dp[start] + travelScore[start][dest]);
                    }
                }
            }
            dp = move(ndp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
