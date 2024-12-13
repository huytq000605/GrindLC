class Solution {
public:
    long long findScore(vector<int>& nums) {
        vector<pair<int, int>> numsi(nums.size());
        for(int i{}; i < nums.size(); ++i) {
            numsi[i] = {nums[i], i};
        }
        sort(numsi.begin(), numsi.end());
        long long result{};
        for(auto [_, i]: numsi) {
            if(!nums[i]) continue;
            result += nums[i];
            for(int j = max(0, i-1); j <= i+1 && j < nums.size(); ++j) nums[j] = 0;
        }
        return result;
    }
};
