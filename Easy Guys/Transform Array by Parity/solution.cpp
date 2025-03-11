class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        vector<int> result(nums.size());
        for(int i{}; i < nums.size(); ++i) result[i] = nums[i] & 1;
        sort(result.begin(), result.end());
        return result;
    }
};
