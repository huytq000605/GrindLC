class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> result(nums.size());
        int prefix = 0;
        int s = accumulate(begin(nums), end(nums), 0);
        for(int i = 0; i < nums.size(); ++i) {
            result[i] = abs(s - prefix - nums[i] - prefix);
            prefix += nums[i];
        }
        return result;
    }
};
