class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        nums[0] -= k;
        int result{1};
        for(int i{1}; i < nums.size(); ++i) {
            if(nums[i] > nums[i-1]) nums[i] = max(nums[i-1] + 1, nums[i] - k);
            else if(nums[i] + k > nums[i-1]) nums[i] = nums[i-1] + 1;
            else nums[i] = nums[i-1];
            result += nums[i] != nums[i-1];
        }
        return result;
    }
};
