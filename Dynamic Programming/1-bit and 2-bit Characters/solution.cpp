class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        if(bits.size() == 1) return true;
        // could end at two previous indexes
        vector<int> dp(2);
        dp[0] = 1;
        dp[1] = !bits[0];
        for(int i = 1; i < bits.size()-1; ++i) {
            vector<int> ndp(2);
            if(!bits[i]) {
                if(dp[1]) ndp[1] = 1;
                else if(dp[0] && bits[i-1]) ndp[1] = 1;
            } else {
                if(dp[0] && bits[i-1]) ndp[1] = 1;
            }
            ndp[0] = dp[1];
            dp = ndp;
        }
        return dp.back();
    }
};
