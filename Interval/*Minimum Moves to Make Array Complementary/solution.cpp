class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<int> delta(limit*2+2);
        for(int i = 0; i < n / 2; ++i) {
            int mn = min(nums[i], nums[n-1-i]);
            int mx = max(nums[i], nums[n-1-i]);

            delta[2] += 2;
            delta[mn+1] -= 1;
            delta[mn+mx] -= 1;
            delta[mn+mx+1] += 1;
            delta[mx+limit+1] += 1;
        }
        int moves = 0;
        int result = n;
        for(int target = 2; target < limit*2+1; ++target) {
            moves += delta[target];
            result = min(result, moves);
        }
        return result;
    }
};
