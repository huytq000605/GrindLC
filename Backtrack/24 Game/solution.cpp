class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> nums(cards.begin(), cards.end());
        auto dfs = [](this auto&& dfs, vector<double>& nums) {
            if(nums.size() == 1) {
                return abs(nums[0] - 24) < 1e-8;
            }
            for(int i = 0; i < nums.size(); ++i) {
                for(int j = i+1; j < nums.size(); ++j) {
                    vector<double> next_nums;
                    for(int k = 0; k < nums.size(); ++k) {
                        if(k != i && k != j) next_nums.push_back(nums[k]);
                    }
                    next_nums.push_back(nums[i] + nums[j]);
                    if(dfs(next_nums)) return true;
                    for(double last: {nums[i] * nums[j], nums[i] - nums[j], nums[j] - nums[i], nums[i] / nums[j], nums[j] / nums[i]}) {
                        next_nums.back() = last;
                        if(dfs(next_nums)) return true;
                    }
                }
            }
            return false;
        };
        return dfs(nums);
    }
};
