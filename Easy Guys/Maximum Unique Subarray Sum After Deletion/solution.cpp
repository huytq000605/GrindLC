class Solution {
public:
    int maxSum(vector<int>& nums) {
        int result = 0;
        vector<int> seen(101);
        bool no_positive = true;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] > 0 && !seen[nums[i]]) {
                seen[nums[i]] = 1;
                result += nums[i];
                no_positive = false;
            }
        }
        if(no_positive) return *max_element(nums.begin(), nums.end());
        return result;
    }
};
