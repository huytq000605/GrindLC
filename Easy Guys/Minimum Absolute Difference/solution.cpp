class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& nums) {
        sort(begin(nums), end(nums));
        vector<vector<int>> result;
        int target = INT_MAX;
        for(int i = 0; i < nums.size() - 1; ++i) {
            if(nums[i+1] - nums[i] < target) {
                result = {{nums[i], nums[i+1]}};
                target = nums[i+1] - nums[i];
            } else if(nums[i+1] - nums[i] == target) {
                result.push_back({nums[i], nums[i+1]});
            }
        }
        return result;
    }
};
