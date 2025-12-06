class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        int MOD = 1e9 +7;
        deque<int> maxq, minq;
        vector<int> dp(nums.size() + 1);
        dp[0] = 1;
        // dp[x] = number of ways to partition first x elements
        int acc = 1;
        for(int j = 0, i = 0; i < nums.size(); ++i) {
            while(!maxq.empty() && nums[i] > nums[maxq.back()]) {
                maxq.pop_back();
            }
            maxq.push_back(i);
            while(!minq.empty() && nums[i] < nums[minq.back()]) {
                minq.pop_back();
            }
            minq.push_back(i);
            while(nums[maxq.front()] - nums[minq.front()] > k) {
                acc = (acc - dp[j++] + MOD) % MOD;
                if(maxq.front() < j) maxq.pop_front();
                if(minq.front() < j) minq.pop_front();
            }
            dp[i+1] = acc;
            acc = (acc + dp[i+1]) % MOD;
        }
        return dp.back();
    }
};
