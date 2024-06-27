class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        for(int mask = 0; mask < 1 << nums.size(); mask++) {
            vector<int> subset;
            for(int i = 0; i < nums.size(); i++) {
                if((mask >> i) & 1) {
                    subset.emplace_back(nums[i]);
                }
            }
            result.emplace_back(subset);
        }
        return result;
    }
};
