class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        return lower_bound(nums.begin(), nums.end(), target+1) - lower_bound(nums.begin(), nums.end(), target) > nums.size() / 2;
    }
};
