class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        for(int i{}; i < nums.size(); ++i) {
            int target_idx = ((i + nums[i]) % n + n) % n;
            result[i] = nums[target_idx];
        }
        return result;
    }
};
