class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        vector<long long> dp(30, 0);
        for(int d = days.front(), i{}; d <= days.back(); ++d) {
            if(d == days[i]) {
                dp[d%30] = min({dp[(d-1+30)%30] + costs[0], dp[(d-7+30)%30] + costs[1], dp[(d-30+30)%30] + costs[2]});
                ++i;
            } else {
                dp[d%30] = dp[(d-1+30)%30];
            }
        }
        return dp[days.back() % 30];
    }
};
