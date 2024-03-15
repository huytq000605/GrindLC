class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(nums.size(), 1);
        int cur = 1;
        for(int i = 0; i < nums.size(); i++) {
            result[i] *= cur;
            cur *= nums[i];
        }
        cur = 1;
        for(int i = n-1; i >= 0; i--) {
            result[i] *= cur;
            cur *= nums[i];
        }
        return result;
    }
};
