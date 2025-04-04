class Solution {
public:
    int maxSum(vector<int>& nums) {
        int result = 0;
        unordered_set<int> seen;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] > 0 && seen.find(nums[i]) == seen.end()) {
                seen.emplace(nums[i]);
                result += nums[i];
            }
        }
        if(seen.empty()) return *max_element(nums.begin(), nums.end());
        return result;
    }
};
