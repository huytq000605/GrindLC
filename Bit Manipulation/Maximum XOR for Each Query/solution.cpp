class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int xr = 0;
        for(int num: nums) xr ^= num;
        vector<int> result;
        int target = (1 << maximumBit)-1;
        for(int i = nums.size() - 1; i >= 0; --i) {
            result.emplace_back(xr ^ target);
            xr ^= nums[i];
        }
        return result;
    }
};
