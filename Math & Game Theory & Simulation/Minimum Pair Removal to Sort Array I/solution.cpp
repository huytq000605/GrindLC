class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int result = 0;
        while(!is_sorted(nums.begin(), nums.end())) {
            int s = nums[0] + nums[1], j = 0;
            for(int i = 1; i < nums.size()-1; ++i) {
                if(nums[i] + nums[i+1] < s) {
                    s = nums[i] + nums[i+1];
                    j = i;
                }
            }
            vector<int> nnums;
            for(int i = 0; i < nums.size(); ++i) {
                nnums.emplace_back(nums[i]);
                if(i == j) nnums.back() += nums[++i];
            }
            nums = nnums;
            ++result;
        }
        
        return result;
    }
};
